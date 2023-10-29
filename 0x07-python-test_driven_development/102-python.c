#include <Python.h>
#include <stdio.h>
/**
 * print_python_string - function prints python string
 * @p: pointer to the python object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	const char *str;
	const char *type;

	printf("[.] string object info\n");

	/* Check if p is a string object */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Determine if the string is in compact ascii or compact unicode format */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	/* Get the length and value of the string object */
	str = PyUnicode_AsUTF8AndSize(p, &len);

	printf("  type: %s\n", type);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", str);
}
