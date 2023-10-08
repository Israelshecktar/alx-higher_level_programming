#include <python3.h>
#include <object.h>
#include <listobject.h>
/**
* print_python_list_info - function prints python list info
* @p: pointer to a python list
* Return: Nothing
*/
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(list);
	Py_ssize_t alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyObject *type = PyObject_Type(item);

		printf("Element %ld: %s\n", i, ((PyTypeObject *)type)->tp_name);
		Py_DECREF(type);
	}
}
