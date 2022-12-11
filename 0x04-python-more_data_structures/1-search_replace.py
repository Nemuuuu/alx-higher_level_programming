def search_replace(my_list, search, replace):
   my_list[:] = [replace if x == search else x for x in my_list]
   return my_list