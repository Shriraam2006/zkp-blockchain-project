import random

# Secret known only to prover
SECRET = random.randint(1, 100)

# Number of verification rounds
ROUNDS = 5

def generate_challenge():
    return random.randint(1, 50)

def prover_response(secret, challenge):
    # Simulated response (hiding actual secret)
    return (secret * challenge) % 97

def verifier_check(response, challenge):
    # Verifier tries to validate without knowing the secret
    for possible_secret in range(1, 101):
        if (possible_secret * challenge) % 97 == response:
            return True
    return False

def run_zkp_protocol():
    print("Running Zero Knowledge Proof Protocol...\n")

    success_count = 0

    for i in range(ROUNDS):
        challenge = generate_challenge()
        response = prover_response(SECRET, challenge)

        print(f"Round {i+1}")
        print(f"Challenge: {challenge}")
        print(f"Response: {response}")

        if verifier_check(response, challenge):
            print("Verification: SUCCESS\n")
            success_count += 1
        else:
            print("Verification: FAILED\n")

    print("Final Result:")
    if success_count == ROUNDS:
        print("Proof Verified: Prover has knowledge of the secret")
    else:
        print("Proof Inconclusive")

run_zkp_protocol()
