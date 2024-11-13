import math
from scipy.optimize import minimize_scalar

def find_entropy():
    # Given probabilities
    P_a1 = 0.33
    P_b1_given_a1 = 0.76
    P_b2_given_a2 = 0.66

    # Compute P(a2)
    P_a2 = 1 - P_a1

    # Compute conditional probabilities
    P_b2_given_a1 = 1 - P_b1_given_a1
    P_b1_given_a2 = 1 - P_b2_given_a2

    # Compute P(b1) and P(b2)
    P_b1 = P_b1_given_a1 * P_a1 + P_b1_given_a2 * P_a2
    P_b2 = P_b2_given_a1 * P_a1 + P_b2_given_a2 * P_a2

    # Helper function to compute entropy
    def entropy(*probs):
        return -sum(p * math.log2(p) for p in probs if p > 0)

    # Compute H(B)
    H_B = entropy(P_b1, P_b2)

    # Compute H(B|a1)
    H_B_given_a1 = entropy(P_b1_given_a1, P_b2_given_a1)

    # Compute H(B|a2)
    H_B_given_a2 = entropy(P_b1_given_a2, P_b2_given_a2)

    # Compute H(B|A)
    H_B_given_A = P_a1 * H_B_given_a1 + P_a2 * H_B_given_a2

    # Compute H(A)
    H_A = entropy(P_a1, P_a2)

    # Compute H(A|b1)
    P_a1_given_b1 = (P_b1_given_a1 * P_a1) / P_b1
    P_a2_given_b1 = (P_b1_given_a2 * P_a2) / P_b1
    H_A_given_b1 = entropy(P_a1_given_b1, P_a2_given_b1)

    # Compute H(A|b2)
    P_a1_given_b2 = (P_b2_given_a1 * P_a1) / P_b2
    P_a2_given_b2 = (P_b2_given_a2 * P_a2) / P_b2
    H_A_given_b2 = entropy(P_a1_given_b2, P_a2_given_b2)

    # Compute H(A|B)
    H_A_given_B = P_b1 * H_A_given_b1 + P_b2 * H_A_given_b2

    return H_B, H_B_given_A, H_A, H_A_given_B

def H(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)

def H_prime(x):
    return math.log2(1 / x - 1)

def H_B_given_A(p):
    return 0.5 * p + 0.1

def H_B(p):
    return H(0.4 * p + 0.1)

def channel_capacity(p):
    return H_B(p) - H_B_given_A(p)

def find_p():
    # Minimize the negative channel capacity to find the maximum channel capacity
    result = minimize_scalar(lambda p: -channel_capacity(p), bounds=(0, 1), method='bounded')
    p_optimal = result.x
    p_optimal = round(p_optimal, 2)
    C_AB = round(channel_capacity(p_optimal), 2)
    
    # Print the result
    print(f"The approximate value of p that achieves the channel capacity is: {p_optimal}")
    print(f"The channel capacity C(A,B) is: {C_AB}")

def find_info():
    # Given entropies
    H_A = 0.42
    H_B = 0.2
    H_A_B = 0.58

    # Compute mutual information I(A;B)
    I_A_B = H_A + H_B - H_A_B
    I_A_B = round(I_A_B, 2)
    print(f"The mutual information I(A;B) is: {I_A_B}")

def find_joint():
    # Given entropies
    H_A = 0.5
    H_B = 0.71
    I_A_B = 0.46

    # Compute joint entropy H(A,B)
    H_A_B = H_A + H_B - I_A_B
    H_A_B = round(H_A_B, 2)
    print(f"The joint entropy H(A,B) is: {H_A_B}")

def main():
    mode = input("Enter mode (find entropy, find p, find info, find joint): ").strip().lower()
    if mode == "find entropy":
        print(find_entropy())
    elif mode == "find p":
        find_p()
    elif mode == "find info":
        find_info()
    elif mode == "find joint":
        find_joint()
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()