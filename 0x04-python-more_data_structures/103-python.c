#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - function prints pyhton bytes
* @p: pointer to python bytes
* Return: Nothing
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size;
	Py_ssize_t i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", size + 1 < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02hhx", str[i]);

		if (i + 1 < size + 1 && i + 1 < 10)
			printf(" ");
	}

	printf("\n");
}
/**
* print_python_list - function print python list
* @p: pointer to python list
* Return: Nothing
*/
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	long int i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		/* If item is bytes type, print its info */
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}
