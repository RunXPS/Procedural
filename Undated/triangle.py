class triangle():
    #My Ways
    #Way 1
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
    print("******\n")
    #Way 2
    print("*\n**\n***\n****\n*****\n******")

    #Class' Ways
    #Way 1 - Eric
    for i in range (6):
        print("*" * (i+1))
    #Way 2 - Santosh
    star = ""
    for i in range (6):
        star += "*"
        print(star)
    #Way 3 - Pratham
    print("*","**", "***", "****", "*****", "******", sep = "\n")
    #Way 4 - Chris S.
    print('''*
**
***
****
*****
******''')
    #Tree Triangle
    #My Way
    print("      *")
    print("     * *")
    print("    * * *")
    print("   * * * *")
    print("  * * * * *")
    print(" * * * * * *")
    print("     * *")
    print("     * *")

    #Class Ways
    #Shreenidhi
    print("""
          *
         * *
        * * *
       * * * *
      * * * * *
     * * * * * *
         * *
         * *
    """)