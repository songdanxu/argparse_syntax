'''
Auther:Qi Guangyuan
Data:2021-12-3
Contact:qiguangyuan0406@163.com
Study Script:Use argparse to pass in command line parameters
'''

import argparse
'''
We call this method as the parameter parser method,and its use can be divided into three basic steps:
1.Instantiate the parameter parser;
2.Add parameter settings;
3.Parse the obtained parameters
'''

parser=argparse.ArgumentParser(description='An argparse example')
# Instantiate the parameter parser.

parser.add_argument('--method','-m',choices=['add','multiple'],help='choose whether to add or multiply')
parser.add_argument('-a',default=1,type=int,help='The first number')
parser.add_argument('-b',default=2,type=int,help='The second number')
'''
Important and commonly used parameters
1.names:the name of the parameter.A required parameter.It is ranked first(if there are multiple names,it will be ranked first).
        Usually,the "short format" or/and the "long format" are used.
        Such as:--version and -v.
2.type:The type to which the command line parameter should be converted,such as bool,int,float,str,etc.
3.default:When the parameter does not appear in the commend line,use this default value.
        Such as:parser.add_argument("-a",default='1')
                If the -a parameter is not passed in the command line,the value if this parameter will be set to 1.
4.action:Specify the action of the parameter,that is how to deal with this parameter.
        There are many actions to choose,which are not used temporarily.
5.choices:This parameter accepts a list as a value,the parameter value is limited to this list.
6.help:The help description for this parameter will be printed in the help file.
'''
args=parser.parse_args()
'''
Use the ArgumentParser.parse_args method to parse the obtained parameters and return the parsed result.
Then you can use the name specified for each parameter in the settings to get their value.
For example,use args.method to get the value obtained by the --method parameter. 
'''
if args.method == 'add':
    print(args.a+args.b)
else:
    print(args.a*args.b)

'''
Some examples of calls:

>python argparse_syntax.py
2

>python argparse_syntax.py --help
usage: argparse_syntax.py [-h] [--method {add,multiple}] [-a A] [-b B]

An argparse example

optional arguments:
  -h, --help            show this help message and exit
  --method {add,multiple}, -m {add,multiple}
                        choose whether to add or multiply
  -a A                  The first number
  -b B                  The second number
  
python argparse_syntax.py --method add -a 10 -b 20
30
'''