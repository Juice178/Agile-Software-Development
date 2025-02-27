from policy import Policy, AddPolicy, SubtractPolicy
import fire


def main(num_1: int, num_2: int) -> None:
    p_a: Policy = AddPolicy(num_1, num_2)
    p_a.policy_function()

    p_b: Policy = SubtractPolicy(num_1, num_2)
    p_b.policy_function()


if __name__ == "__main__":
    fire.Fire(main)