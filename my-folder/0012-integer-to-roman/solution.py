class Solution(object):
    def intToRoman(self,number):
        returnString = ""
        if number//1000:
            returnString += "M"*(number//1000)
            number = number%1000

        if number//900:
            returnString += "CM"
            number = number%900
        elif  number//500:
            number = number%500
            returnString+="D"
            if number//100:
                returnString += "C"*(number//100)
            number = number%100
        elif number//400:
            number = number%400
            returnString += "CD"

        if number/100:
            returnString += "C"*(number//100)
        number = number%100


        if number//90:
            returnString += "XC"
            number = number%90
        elif  number//50:
            number = number%50
            returnString+="L"
            if number//10:
                returnString += "X"*(number//10)
            number = number%10
        elif number//40:
            number = number%40
            returnString += "XL"

        if number/10:
            returnString += "X"*(number//10)
            number = number%10 

        if number//9:
            returnString += "IX"
            number = number%9
        elif  number//5:
            number = number%5
            returnString+="V"
            if number//1:
                returnString += "I"*(number//1)
            number = number%1
        elif number//4:
            number = number%4
            returnString += "IV"

        if number/1:
            returnString += "I"*(number//1) 
        
        return returnString
        """
        :type num: int
        :rtype: str
        """
        
