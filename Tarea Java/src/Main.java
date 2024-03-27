import javax.swing.*;
import java.io.*;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static <string> void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);
        BufferedWriter writer = new BufferedWriter(new FileWriter( "Lista de alumnos.txt"));
        BufferedReader reader = new BufferedReader( new FileReader("Lista de alumnos.txt"));
        String header = "-------------------------------\n";
        String message = "Bienvenidos al programa\n¿Qué función desea realizar?\n";
        String message2 = "\t1.Añadir nombres.\n\t2.Mostrar nombres\n\t3.Salir\n";

        boolean control = true ;
        String students="";
        while (control) {


            System.out.println(header);
            System.out.println(message);
            System.out.println(header);
            System.out.println(message2);
            System.out.println(header);
            System.out.println("Escriba aquí: ");
            String selection = scanner.nextLine();

            switch (selection) {
                case "1":
                    System.out.println("Escriba los nombres separados por comas: ");
                    students = scanner.nextLine();
                    writer.write("Listado de alumnos inscritos al curso: ");
                    writer.newLine();
                    String[] allStudents = students.split(",");

                    for (int i=0; i < allStudents.length; i++) {
                        writer.write(allStudents[i].trim());
                        writer.newLine();
                    }
                    writer.close();
                    break;
                case "2":
                    if (students.isEmpty()){
                        System.out.println("Aún No hay ningún alumno inscrito a este curso.");

                    } else {
                        String line;
                        while ( (line = reader.readLine()) != null)  {
                            System.out.println(line);
                        }
                        reader.close();
                    }
                    break;
                case "3":
                    control = false;
                    System.out.println("El programa ha finalizado");
                    break;

            }
    }
}
}