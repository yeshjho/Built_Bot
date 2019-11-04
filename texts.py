class TEXT:
    class TESTCASE:
        INPUT = "IN"
        OUTPUT = "OUT"
        INSERT = "INSERT"
        TERMINATION = "TERMINATION"
        EXCEPTION = "EXCEPTION"

    class EMBED:
        TEST_RESULT = "Test Result: "
        TEST_RESULT_WITH_ERROR = " with errors"
        PASSED_COUNT = "Passed Tests: "
        FAILED_COUNT = "Failed Tests: "
        ERROR_COUNT = "Other Errors: "

        TEST_NUM = "Test #"
        TEST_PASSED = "Passed"
        TEST_FAILED = "Failed"
        INPUT = "Input"
        EXPECTED_OUTPUT = "Expected Output"
        ACTUAL_OUTPUT = "Actual Output"

        ERROR_NUM = "Error #"

        SEE_PASSED = "P"
        SEE_FAILED = "F"
        SEE_ERROR = "E"
        SEE_ALL = "A"

        ACTUAL_NO_TERMINATION = "(Didn't terminate successfully)"
        ACTUAL_NO_EXCEPTION = "(Didn't raise an exception)"

    class SAVE:
        BLOCKED = "Oops! You're on the blacklist!"

        SUPPORTED_FILE_EXTENSION = "Only cpp files are supported"
        RECEIVED = "File received"

        COOL_TIME_1 = "Whoa, too fast!\nYou have to wait for `"
        COOL_TIME_2 = " minutes and "
        COOL_TIME_3 = " seconds` for another attempt"

        QUERY_ASSIGNMENT = "What assignment is this for? Please enter a number"
        TRY_AGAIN = "Please try again"

    class COMPILE:
        COMPILING = "Compiling..."
        SUCCESS = "Compilation Succeeded"
        FAIL = ":no_entry: Compilation Failed"
        TIMEOUT = "Timed out"

    class TEST:
        TESTING = "Testing..."
        COMPLETE = "Testing complete"
        FAIL = "Testing failed.\nIt might be my problem, please try again! Resetting your cooltime..."
        
        UNICODE_ERROR = "Error testing failed. Your file must be encoded with UTF-8.\nSkipping error tests..."

        ZERO_PERCENT_1 = [":expressionless:", ":unamused:", ":disappointed:", ":worried:", ":frowning2:",
                          ":persevere:", ":confounded:", ":tired_face:", ":weary:", ":scream:", ":cold_sweat:",
                          ":sob:", ":dizzy_face:", ":poop:", ":head_bandage:"]
        ZERO_PERCENT_2 = "You've passed nothing! You may not examine any of the test cases...\nThink for yourself!"

        MIDDLE = [":neutral_face:", ":rolling_eyes:", ":thinking:", ":confused:", ":slight_frown:",
                  ":disappointed_relieved:", ":sweat:", ":fearful:", ":cry:", ":flushed:", ":pensive:"]

        HUNDRED = [":grinning:", ":smiley:", ":wink:", ":blush:", ":sunglasses:", ":+1:", ":smirk:",
                   ":yum:", ":slight_smile:", ":laughing:", ":innocent:", ":hugging:"]

        SEE_PASSED = "Type :regional_indicator_p: to examine what tests you've passed\n"
        SEE_FAILED = "Type :regional_indicator_f: to examine what tests you've failed\n"
        SEE_ERROR = "Type :regional_indicator_e: to examine what errors you've got\n"
        SEE_ALL = "Type :regional_indicator_a: to examine all"

    class OTHER:
        TESTING = "Sorry! Currently Testing!"

    class COMMAND:
        COMMAND_HELP = "help"
        COMMAND_COOLTIME = "cooltime"
        COMMAND_VERSION = "version"
        COMMAND_PERMISSION = "permission"
        COMMAND_ATTRIBUTE = "attribute"
        COMMAND_RELOAD = "reload"

        PERMISSION_COMMAND_SEE_ALL = "ALL"
        PERMISSION_OTHER = "OTHER"

        SUCCESS = "Successfully executed the command"
        NO_PERMISSION = "You're not allowed to use this command!"
        INVALID_ARGUMENT = "Arguments are invalid"
        UNKNOWN_COMMAND = "Unknown command\nType `>>>help` to see all available commands"

    class ATTRIBUTES:
        COOLTIME = "COOLTIME"
