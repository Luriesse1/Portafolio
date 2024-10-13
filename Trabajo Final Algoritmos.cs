using System;

class Program {
  public static void Main (string[] args) 
  {
    //Variables de entrada
    int cantidadEmpleados;
    
    //Variables de salida
    int totaldeventas=0;
    double totalpromedios=0;
    
    //Variables de trabajo
    int[,] matrizDeEnteros = new int[10,4];
    double[] vectorPromedios = new double[10];
    string[] vectorNombres = new string[10];
    int[] auxiliarEnteros= new int[10];
    double auxiliarReales;
    string auxiliarNombres;
    int i;
    int c;
    int j;
    int k;
    double totalpromediossuma=0;
    
    //Ingresar y validar el numero de empleados
    do{
      Console.Write("Ingrese la cantidad de empleados: ");
      cantidadEmpleados = int.Parse(Console.ReadLine());
    }while(cantidadEmpleados<7 || cantidadEmpleados>10);
    
    //Ingresar y validar los datos de los empleados(Nombre, y numero de ventas por mes)
    for(i=0; i<=cantidadEmpleados-1; i++)
    {
      do{
        Console.Write("Ingrese El nombre del empleado N° " + (i+1) + ": ");
         vectorNombres[i] = Console.ReadLine();
      }while(vectorNombres[i]=="");
      do{
        Console.Write("Ingrese la cantidad de ventas del empleado N° " + (i+1)+" en el mes de Enero: ");
        matrizDeEnteros[i,0] = int.Parse(Console.ReadLine());
      }while(matrizDeEnteros[i,0]<0);
      do{
        Console.Write("Ingrese la cantidad de ventas del empleado N° " + (i+1)+" en el mes de Febrero: ");
        matrizDeEnteros[i,1] = int.Parse(Console.ReadLine());
      }while(matrizDeEnteros[i,1]<0);
      do{
        Console.Write("Ingrese la cantidad de ventas del empleado N° " + (i+1)+" en el mes de Marzo: ");
        matrizDeEnteros[i,2] = int.Parse(Console.ReadLine());
      }while(matrizDeEnteros[i,2]<0);
      matrizDeEnteros[i,3] = matrizDeEnteros[i,0] + matrizDeEnteros[i,1] + matrizDeEnteros[i,2];
      totaldeventas = totaldeventas + matrizDeEnteros[i,3];
      vectorPromedios[i] = matrizDeEnteros[i,3]/3.0;
      totalpromediossuma = totalpromediossuma + vectorPromedios[i];
    }
    
    // Calculo del promedio total de ventas de todos los vendedores
    totalpromedios = totalpromediossuma/cantidadEmpleados;
    
    // Ordenamiento burbuja por ventas totales en matrizDeEnteros, vectorPromedios y vectorNombres
    for (c = 0; c < cantidadEmpleados - 1; c++)
    {
      for (j = 0; j < cantidadEmpleados - c - 1; j++)
      {
        do{
          // Intercambiar en matrizDeEnteros
           for (k = 0; k < 4; k++)
          {
            auxiliarEnteros[j] = matrizDeEnteros[j,k];
            matrizDeEnteros[j,k] = matrizDeEnteros[j + 1,k];
            matrizDeEnteros[j + 1,k] = auxiliarEnteros[j];
          }

           // Intercambiar en vectorPromedios
           auxiliarReales = vectorPromedios[j];
           vectorPromedios[j] = vectorPromedios[j + 1];
           vectorPromedios[j + 1] = auxiliarReales;

           // Intercambiar en vectorNombres
           auxiliarNombres = vectorNombres[j];
           vectorNombres[j] = vectorNombres[j + 1];
           vectorNombres[j + 1] = auxiliarNombres;
        }while(matrizDeEnteros[j, 3] < matrizDeEnteros[j + 1, 3]);
      }
    }
    
    // Mostrar los datos
    Console.WriteLine("Total de ventas realizadas por todos los agentes es: " + totaldeventas);
    Console.WriteLine("Total de promedios de todos los agentes es: " + totalpromedios);
    Console.WriteLine("La menor venta de todos los agentes es: " + matrizDeEnteros[cantidadEmpleados-1,3]);
    Console.WriteLine("La mayor venta de todos los agentes es: " + matrizDeEnteros[0,3]);
    Console.WriteLine("El agente con mas ventas es: " + vectorNombres);
  }
}