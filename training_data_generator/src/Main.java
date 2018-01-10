import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        String message;
        Scanner sc=new Scanner(System.in);
        System.out.println("How Many Exampels Do You Have?");
        int NumExanpels= sc.nextInt();
        JSONObject JsonFile = new JSONObject();
        JSONObject json = new JSONObject();
        try {
            JSONArray array= CreateJsonArray(NumExanpels);
            json.put("common_examples", array);
            JsonFile.put("nlu_data",json);
            message = JsonFile.toString(4);

            String FileName = "data_nlu.json";
            BufferedWriter writer = null;
            try {
                writer = new BufferedWriter(new FileWriter(FileName));
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                writer.write(message);
            } catch (IOException e) {
                e.printStackTrace();
            }

            try {
                writer.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println(message);

        } catch (JSONException e) {
            e.printStackTrace();
        }


    }

    public static JSONArray CreateEntityArray(int NumEntities) throws JSONException {
        JSONArray array = new JSONArray();
        for(int i=0; i< NumEntities; i++){
            Scanner sc=new Scanner(System.in);
            System.out.println("Enter The entity");
            String Entity=sc.nextLine();
            System.out.println("Enter The entity value");
            String EntityValue=sc.nextLine();
            System.out.println("When it is start?");
            int Start= sc.nextInt();
            System.out.println("When it is end?");
            int End= sc.nextInt();

            JSONObject item = CreatEntityObject(Entity,EntityValue,Start,End);
            array.put(item);
        }
        return array;
    }

    public static JSONArray CreateJsonArray(int NumExamples) throws JSONException {
        JSONArray array = new JSONArray();
        Scanner sc=new Scanner(System.in);
        for(int i=0; i< NumExamples; i++){
            System.out.println("Enter The Text");
            String TextValue=sc.nextLine();
            System.out.println("Enter The Intent");
            String IntentValue=sc.nextLine();
            JSONObject item = CreatJsonObject(TextValue,IntentValue);
            array.put(item);
        }
        return array;
    }

    public static JSONObject CreatJsonObject(String TextValue,String IntentValue) throws JSONException {
        JSONObject item = new JSONObject();
        item.put("text", TextValue);
        item.put("intent", IntentValue);
        Scanner sc=new Scanner(System.in);
        System.out.println("How Many Entities Do You have?");
        int NumEntities= sc.nextInt();
        JSONArray EntitiesArray= CreateEntityArray(NumEntities);
        item.put("entities", EntitiesArray);
        return item;
    }
    public static JSONObject CreatEntityObject(String Entity,String EntityValue,int Start,int End)throws JSONException {
        JSONObject item = new JSONObject();
        item.put("entity", Entity);
        item.put("value", EntityValue);
        item.put("start", Start);
        item.put("end", End);
        return item;
    }
}
