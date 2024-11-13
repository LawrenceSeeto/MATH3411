import math

def conditional_entropy(M, j):
    """Calculate H(S|s_j) for a given state j."""
    H_sj = 0.0
    for i in range(len(M)):
        p_si_given_sj = M[i][j]
        if p_si_given_sj > 0:
            H_sj -= p_si_given_sj * math.log(p_si_given_sj, 2)  # Logarithm base 2
    return H_sj

def markov_entropy(M, P):
    """Calculate Markov entropy H_M(S) given transition matrix M and equilibrium distribution P."""
    H_M = 0.0
    for j in range(len(P)):
        H_sj = conditional_entropy(M, j)
        H_M += P[j] * H_sj
    H_M = round(H_M, 2)
    return H_M

# Define the transition matrix M as a list of lists
M = [
    [0.65, 0.05],
    [0.35, 0.95],
]

# Define the equilibrium distribution P as a list
P = [1/8, 7/8]

# Now you can call the function
entropy = markov_entropy(M, P)
print(f"Markov Entropy: {entropy}")
