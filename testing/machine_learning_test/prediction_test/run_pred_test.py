import argparse
from testing.machine_learning_test.prediction_test import pred_tests

parser = argparse.ArgumentParser()
parser.add_argument("-t",
                    "--test",
                    type=str,
                    default='all',
                    help="""different types of tests.
                    \nArgs: all, pred, news, api (default all).""")

args = parser.parse_args()
args.test = "all"

if args.test == 'all':
    pred_tests.run_test(pred_tests.TestPred,
                        '\nRunning all prediction tests...\n')
    pred_tests.run_test(pred_tests.TestNews,
                        '\nRunning all news tests...\n')
    pred_tests.run_test(pred_tests.TestAPI,
                        '\nRunning all api tests...\n')
elif args.test == "pred":
    pred_tests.run_test(pred_tests.TestPred,
                        '\nRunning all prediction tests...\n')
elif args.test == "news":
    pred_tests.run_test(pred_tests.TestNews,
                        '\nRunning all news tests...\n')
elif args.test == "api":
    pred_tests.run_test(pred_tests.TestAPI,
                        '\nRunning all api tests...\n')
else:
    print('Wrong parameter passed to the test option.')
    print('The only valid parameters are:\nall\npred\nnews\napi')
