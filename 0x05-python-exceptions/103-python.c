#include "Python.h"
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	int i = 0;
	Py_ssize_t bytes_size, print_size;
	char *bytes_name;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_size = PyBytes_Size(p);
	bytes_name = PyBytes_AsString(p);

	if (bytes_size > 9)
		print_size = 10;
	else
		print_size = bytes_size + 1;

	printf("  size: %zd\n", bytes_size);
	printf("  trying string: %s\n", bytes_name);
	printf("  first %zd bytes: ", print_size);

	for (i = 0; i < print_size; i++)
	{
		printf("%02x ", bytes_name[i] & 255);
	}
	printf("\n");

/*
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
*/
}

void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	if (PyFloat_AsDouble(p) - (int)PyFloat_AsDouble(p) == 0)
		printf("  value: %g.0\n", PyFloat_AsDouble(p));
	else
		printf("  value: %.16g\n", PyFloat_AsDouble(p));


/*
[.] float object info
  value: 3.14
[-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793]

*/
}
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;
	list = (PyListObject *)p;

	printf("python list info\n");

	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %i: %s\n", i, list->ob_item[i]->ob_type->tp_name);

		if (strcmp("bytes", list->ob_item[i]->ob_type->tp_name) == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp("float", list->ob_item[i]->ob_type->tp_name) == 0)
			print_python_float(list->ob_item[i]);
	}

/*
python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
*/
}


