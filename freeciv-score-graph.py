#!/usr/bin/env python

# creates graphs from freeciv scorelog


#rum imports
import sys
import string
import time
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
import argparse

#set vars
#logfile = "freeciv-score.log"


#def functions

#define main program
def main():

    #read options
    parser = argparse.ArgumentParser(prog='Freeciv score graph')
    parser.add_argument("-l", "--logfile", help="The FreeCIV score file to proccess", nargs='?', 
                        type=argparse.FileType('r'), default='freeciv-score.log')
    parser.add_argument("--listgraphs", help="Lists graphs and there option numbers",
                        action="store_true")
    arg = parser.parse_args()

    #read logfile
    id, tags, players, data, turns = read(arg.logfile)

    #proccess data
    if arg.listgraphs:
        print "{:<8} {:<15}".format('Key','Description')
        print "-"*20
        for tag, descr in tags.iteritems():
            print "{:<8} {:<15}".format(tag, descr)
        print "-"*20
    else:
        print build(id, tags, players, data, turns)
    return



#read log file
def read( logfile ):

    #set working vars
    id = ""
    tags = {}
    turns = []
    players = {}
    data = {}

    #digst the file
    for line in logfile:
        if line[0] in ['\n', "#"]:
            continue

        line = line.strip()
        command, args = string.split(line, maxsplit = 1)

        if command == "id":
            id = args

        elif command == "tag":
            tag, descr = string.split(args, maxsplit = 1)
            tag = int(tag)
            tags[tag] = descr

        elif command == "turn":
            turn, num, descr = string.split(args, maxsplit = 2)
            turn = int(turn)
            num = int(num)
            turns.append(descr)

        elif command == "addplayer":
            turn, pid, name = string.split(args, maxsplit = 2)
            turn = int(turn)
            pid = int(pid)
            players[pid] = name

        elif command == "data":
            turn, tag, pid, value = string.split(args, maxsplit = 3)
            turn = int(turn)
            tag = int(tag)
            pid = int(pid)
            value = float(value)

            if not data.has_key(tag):
                data[tag] = {}
            if not data[tag].has_key(pid):
                data[tag][pid] = []
            data[tag][pid].append(value)

        else:
            continue


    return id, tags, players, data, turns


#build graphs
def build(id, tags, players, data, turns):
    plot = []
    for i in players:
        score = go.Scatter(
            x = turns,
            y = data[25][i],
            name = players[i]
        )
        plot.append(score)
    plot_url = py.plot(plot, filename=id)
    return plot_url

#if not imported run main program
if __name__ == "__main__":
    main()
