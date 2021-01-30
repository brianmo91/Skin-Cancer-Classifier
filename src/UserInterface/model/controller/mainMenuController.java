package UserInterface.model.controller;

import UserInterface.model.model.GuiUtil;
import UserInterface.model.model.UploadFile;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.stage.FileChooser;

import java.io.File;

public class mainMenuController {

    private UploadFile uploadFile;
    private GuiUtil guiUtil;

    @FXML
    private Button mainUploadButton;

    private File fileUploadObject;

    public mainMenuController(){};

    public mainMenuController(File fileUploadObject) {
        this.fileUploadObject = fileUploadObject;
    }

    @FXML
    public void uploadFilePathOfImage(){

        FileChooser filechooser = new FileChooser();
        filechooser.setTitle("Open Resource File");
        filechooser.getExtensionFilters().addAll(
                new FileChooser.ExtensionFilter("Image Files", "*.png", "*.jpg")
        );

        File selectedFile = filechooser.showOpenDialog(null);

        if (selectedFile != null) {
            uploadFile.setFilePath(selectedFile.getAbsolutePath());

            /*TODO
            *implement scene change to neural network menu
            */

        }
        else {
           guiUtil.showAlertForBadImage();
        }
    }


}
