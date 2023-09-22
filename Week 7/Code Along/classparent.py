class parent:
    def __init__(self, req_for_parent):
        self.p_field = req_for_parent
    def obj_as_string(self):
        return f'{self._p_field =}'
    
    def parent_obj_as_string(self):
        return f'{self._p_field = }'
    
class child(parent):
    def __init__(self, req_for_child, req_for_parent):
        super().__init__(req_for_parent)
        self._c_field = req_for_child

    def obj_as_string(self):
        return f' Field values:\n{self._c_field = }\t' + super().obj_as_string() 
    
    def child_obj_as_string(self):
        return f'Field values:\n{self._c_field = }\t' + self.parent_obj_as_string()
    
c = child("For child", "For parent")
print(f'{c.child_obj_as_string()}')
print(f'{c.child_obj_as_string()}')

