#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 50
#define MAX_SIZE_CODE 30
#define MAX_RADIX_SIZE 20


// stack for printing out codes
struct code_node {
    struct code_node *next;
    int data;
};

// Tree from algorithm
struct node {
    struct node *children[MAX_RADIX_SIZE];
    int probability;
};

struct code_node *create_new_code_node(int data);
struct node *create_new_node(int probability, int radix);
int find_average_length(struct node *parent, int radix);
void place_highest(struct node *probability_array[MAX_SIZE], int number);
struct code_node *add_new_node(int data, struct code_node *code_node_head);
int check_children(struct node *parent, int radix);
void print_codes(struct node *parent, int radix, struct code_node *code_node_head);
struct code_node *null_tail(struct code_node *code_node_head);
void free_tree(struct node *parent, int radix);
void swap_entries(struct node *probability_array[MAX_SIZE], int index1, int index2);


int main(void) {
    int radix;
    printf("Please enter the radix (r >= 2): ");
    scanf("%d", &radix);
    
    // Stores probabilities of current generation
    struct node *probability_array[MAX_SIZE];

    printf("Enter the lowest common multiple (n) of probability denominators: ");
    
    int denominator;
    scanf("%d", &denominator);
    printf("Enter numbers X where p = X/n (press control-d when done):\n");
    
    int probability;
    int number = 0;
    while(scanf("%d", &probability) == 1) {
        probability_array[number] = create_new_node(probability, radix);
        place_highest(probability_array, number);
        number++;
    }
    
    // adding dummy sources
    while (number % (radix - 1) != 1 && radix != 2) {
        probability_array[number] = NULL;
        number++;
    }

    number--;
    
    // applying algorithm
    while(number > 0) {
        // adding up last r probabilities
        int add_probability = 0;
        for (int i = 0; i < radix; i++) {
            if (probability_array[number - i] != NULL) {
                add_probability += probability_array[number - i]->probability;
            }
        }

        // making parent node
        struct node *join_node = create_new_node(add_probability, radix);
        
        for (int i = 0; i < radix; i++) {
            join_node->children[i] = probability_array[number - radix + 1 + i];
        }
        
        number -= (radix - 1);
        probability_array[number] = join_node;
        place_highest(probability_array, number);
    }

    // print out results
    printf("Average length is %d/%d\n", find_average_length(probability_array[0], radix), denominator);
    printf("Codes are:\n");
    print_codes(probability_array[0], radix, NULL);

    // dynamic memory management
    free_tree(probability_array[0], radix);
}


// sorts structs on probability key by shifting elements at index number
void place_highest(struct node *probability_array[MAX_SIZE], int number) {
    for (int i = 0; i < number; i++) {
        if (probability_array[i]->probability <= probability_array[number]->probability) {
            swap_entries(probability_array, i, number);
        }
    }    
}


// swaps entries of array
void swap_entries(struct node *probability_array[MAX_SIZE], int index1, int index2) {
    struct node *temp = probability_array[index1];
    probability_array[index1] = probability_array[index2];
    probability_array[index2] = temp;
    return;
}


// forms new node for tree with probability
struct node *create_new_node(int probability, int radix) {
    struct node *new_node = malloc(sizeof(struct node));
    
    for (int i = 0; i < radix; i++) {
        new_node->children[i] = NULL;
    }
    
    new_node->probability = probability;
    
    return new_node;
}


// uses Knuth's theorem to add the probabilities of all non-leaf nodes
int find_average_length(struct node *parent, int radix) {
    if (parent == NULL) {
        return 0;
    } 

    // adds probabilities only if there is at least one child
    int average_length = 0;
    if (check_children(parent, radix)) {
        average_length += parent->probability;
    }

    // adds children probabilities recursively
    for (int i = 0; i < radix; i++) { 
        average_length += find_average_length(parent->children[i], radix);
    }

    return average_length;
}


void print_codes(struct node *parent, int radix, struct code_node *code_node_head) {
    // If the node is a leaf node, print the code stored in the linked list (stack)
    if (!check_children(parent, radix)) {
        for (struct code_node *code_node = code_node_head; code_node != NULL; code_node = code_node->next) {
            printf("%d", code_node->data);
        }
        printf("\n");
    } else {
        // else go through each branch and store code in linked list (stack)
        for (int i = 0; i < radix; i++) {
            if (parent->children[i] != NULL) {
                code_node_head = add_new_node(i, code_node_head);
                print_codes(parent->children[i], radix, code_node_head);
                code_node_head = null_tail(code_node_head);
            }
        }
    }
}


// deletes the last element of a non-empty linked list (stack)
struct code_node *null_tail(struct code_node *code_node_head) {
    if (code_node_head->next == NULL) {
        free(code_node_head);
        code_node_head =  NULL;
    } else {
        struct code_node *current_node = code_node_head;
        while (current_node->next->next != NULL) {
            current_node = current_node->next;
        }

        free(current_node->next);
        current_node->next = NULL;
    }

    return code_node_head;
}


// returns true if the node is a non-leaf node
int check_children(struct node *parent, int radix) {
    for (int i = 0; i < radix; i++) {
        if (parent->children[i] != NULL) {
            return 1;
        }
    }
    return 0;
}


// adds linked list (stack) node with code data to the end of the list
struct code_node *add_new_node(int data, struct code_node *code_node_head) {
    if (code_node_head == NULL) {
        code_node_head = create_new_code_node(data);
    } else {
        struct code_node *code_node = code_node_head;
        while(code_node->next != NULL) {
            code_node = code_node->next;
        }
        code_node->next = create_new_code_node(data);
    }
    return code_node_head;
}


// creates new linked list node containing data
struct code_node *create_new_code_node(int data) {
    struct code_node *new_code_node = malloc(sizeof(struct code_node));
    new_code_node->data = data;
    new_code_node->next = NULL;
    return new_code_node;
}


// recursively frees the tree
void free_tree(struct node *parent, int radix) {
    if (parent != NULL) {
        for(int i = 0; i < radix; i++) {
            free_tree(parent->children[i], radix);
        }
        free(parent);
    } 
    return;
}