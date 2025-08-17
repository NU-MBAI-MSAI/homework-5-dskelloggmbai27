'''
Daren Sia
Version: 1.0
08/16/2025
'''

def is_leap_year(integer):
    if integer % 4 == 0 and integer % 100 != 0 or integer % 400 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_leap_year()