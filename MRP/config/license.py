






TEMPLATE = """
LICENSE PROVIDED BY {fullname}:
{info}
{license}

"""


MIT = """
MIT License

Copyright (c) {year} {fullname}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""



licenses = {"MIT":MIT}
licenseStack = []



def addLicense(year,fullname,license, extraInfo = {}):
	licenseStack.append({"license":license,"year":year,"fullname":fullname,"extra":extraInfo})



addLicense("2025","Lexi Davies", "MIT", extraInfo = {"contribution":"Original Developer","asOff": "29-19-25"})




def GetLicense(index):
	data = licenseStack[index]
	#print(data)
	license = licenses[data["license"]]
	fullname = data["fullname"]
	year = data["year"]
	info = "\n".join([f"{x} : {data['extra'][x]}" for x in data["extra"]])
	#print(info)
	license = license.format(year = year,fullname = fullname)	
	return TEMPLATE.format(license = license, info = info, fullname = fullname)



if __name__ == "__main__":
	print(GetLicense(0))
