package UserInterface.model.model;

import javafx.scene.control.Alert;

/**
 * Created by Victoria on 5/28/2019.
 */
public class GuiUtil {

    public void showAlertForBadImage(){
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Warning alert");
        alert.setHeaderText("Image Selection Error:");
        alert.setContentText("The image you selected to upload contains an error. Please try again or select a different image!");

        alert.showAndWait();
    }

    public GuiUtil() {
    }


}
