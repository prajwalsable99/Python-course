#private #protected #public

class parent:
    planet="earth"              #public     :   simple declaration          publicly available
    _nationality="indian"       #protected  :   give 1 underscore           available in base & inherited class onlyy
    __age=63                    #private    :   give 2 underscore           avialable only in base class


class child(parent):
    def permit(self):
       return f"i can access  {self.planet} as well as {self._nationality} "

    def nopermit(self):
        return f"{self.__age}"

prajwal=child()
print(prajwal.permit())
# print(prajwal.nopermit())   #thow error private are only for declared class not inherited as well as are not gobal

print(prajwal._nationality)