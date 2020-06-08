class Solution:

    def is_palindrome(self, x):
        import math
        if x <= 0:
            return x == 0

        log_answer = math.log10(x)
        total_digits = math.floor(log_answer) + 1
        msd_mask = math.pow(10, total_digits - 1)

        for i in range(total_digits // 2):
            most_sig_digit = x // msd_mask
            ones_place_digit = x % 10

            if most_sig_digit != ones_place_digit:
                return False

            x %= msd_mask  # remove most sig digit
            x //= 10  # remove last sig digit

            msd_mask //= 100  # remove two zero's from the mask

        return True


if __name__ == '__main__':
    test_cases = [(9232, False), (12321, True), (1, True), (-121, False)]
    for tc in test_cases:
        assert tc[1] == Solution().is_palindrome(tc[0])
