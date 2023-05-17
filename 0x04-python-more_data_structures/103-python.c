#include "Python.h"
#include <stdio.h>
#include <string.h>


/**
 * print_python_bytes - is used to print python bytes
 * @p: python object
 * Return: void
 */

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

	while (i < print_size)
	{
		printf("%02x ", bytes_name[i] & 255);
		i++;
	}

	printf("\n");
}



/**
 * print_python_list - is used to print python list
 * @p: python object
 * Return: void
 */

void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;

	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (strcmp("bytes", list->ob_item[i]->ob_type->tp_name) == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}
