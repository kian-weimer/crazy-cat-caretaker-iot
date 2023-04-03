from multiprocessing import Process


# Create a new process with specific function to execute with args.
def example(args):
    print(args)

def run_async(function, *args):
    Process(target=function, args=args).start()

