
def main(arguments):
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.shell as cmd

    from tigr.drawer.drawer import Drawer

    if arguments['--engine'] != 'turtle':
        from tigr.drawer.tkinter_worker import TkinterWorker as Worker
    else:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker

    worker = Worker(
        speed=int(arguments['--speed']),
        pencolor=arguments['--pencolor'],
        pensize=arguments['--pensize'],
    )
    drawer = Drawer(worker)
    if len(arguments['FILES']) > 0:
        if arguments['--parser'] == 'regex':
            from tigr.parser.regex_parser import RegexParser as Parser
        else:
            from tigr.parser.peg_parser import PEGParser as Parser
        from tigr.reader.reader import SourceReader

        parser = Parser(drawer)
        for filename in arguments['FILES']:
            reader = SourceReader(parser, filename)
            reader.go()

        import time
        time.sleep(0.5)
        if arguments['--interactive']:
            from tigr.shell.shell import Shell
            Shell(drawer).cmdloop()
    else:
        cmd.Shell(drawer).cmdloop()
