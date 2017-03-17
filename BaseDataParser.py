#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import time
import curses
import codecs
        
class BaseDataParser(object):
    def __init__(self, extra_params = []):
        self.debug = True
        super(BaseDataParser, self).__init__()
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        self.extra_params = extra_params
        self.current_dict = {}
        
        self.parse_data(codecs.encode("", "utf-8"), 0)
    
    def __del__(self):
        pass
        if (self.debug):
            pass
        else:
            curses.nocbreak()
            self.stdscr.keypad(0)
            curses.echo()
            curses.endwin()
    
    def print_value(self, line, value):
        key_width = 20
        c_type = type(value)
        if (c_type == int):
            self.stdscr.addstr(line + 2, key_width, "%20i" % value)
        elif (c_type == float):
            self.stdscr.addstr(line + 2, key_width, "%20f" % value)
        elif (c_type == str):
            self.stdscr.addstr(line + 2, key_width, "%20s" % value)
        elif (c_type == bytes):
            self.stdscr.addstr(line + 2, key_width, "%20s" % value.decode("utf-8"))
        # elif (c_type == unicode):
        #     self.stdscr.addstr(line + 2, key_width, "%20s" % value)
        else:
            self.stdscr.addstr(line + 2, key_width, "%20s" % "Unknown type: " + str(type(value)))

    def print_stats(self):
        std_len = 8
        height, width = self.stdscr.getmaxyx()
        offset_descr = "Offset: "
        self.stdscr.addstr(0,0, offset_descr)
        self.stdscr.addstr(0,len(offset_descr), "%8i" % self.current_dict["offset"])

        size_descr = "Size: "
        self.stdscr.addstr(0,len(offset_descr) + std_len + 2, size_descr)
        self.stdscr.addstr(0,len(offset_descr) + std_len + 2 + len(size_descr), "%8i" % self.current_dict["size"])

        time_descr = "Time since last: "
        self.stdscr.addstr(0,len(offset_descr) + 2*std_len + 2 + len(size_descr) + 2, time_descr)
        self.stdscr.addstr(0,len(offset_descr) + 2*std_len + 2 + len(size_descr) + 2 + len(time_descr), "%6.1f" % (time.time() - self.current_dict["time"]))
        self.stdscr.addstr(1,0, "="*width)
        
        ctr = 0
        for key in self.extra_params:
            self.stdscr.addstr(ctr + 2, 0, " " * width)
            if (key == "time" or key == "offset" or key == "size"):
                pass
            else:
                self.stdscr.addstr(ctr + 2, 0, key)
                if (key in self.current_dict):
                    c_value = self.current_dict[key]
                    c_type = type(c_value)
                    if (c_type == list):
                        ctr += 1
                        for c_itm in c_value:
                            self.print_value(ctr, c_itm)
                            ctr += 1
                    else:
                        self.print_value(ctr, c_value)
                else:
                    self.print_value(ctr, "n/a")
                ctr += 1
        
        self.stdscr.refresh()
    
    def my_fb_parser(self, data):
        return {}
    
    def parse_data(self, data, offset):
        start_dict = {}
        start_dict["time"] = time.time()
        start_dict["offset"] = offset
        start_dict["size"] = len(data)
        if (len(data)!= 0):
            self.current_dict = dict(start_dict, **self.my_fb_parser(data))
        else:
            self.current_dict = start_dict
        self.print_stats()
    
    def no_data(self):
        self.print_stats()
