package UserInterface.model.model;

/**
 *
 */
public class UploadFile {

    private String filePath = null;
    private Boolean googleNet = false;
    private Boolean vggNet = false;
    private Boolean resNet = false;
    private Boolean selectAll = false;

    public UploadFile(String filePath){
        this.filePath = filePath;
    }

    public UploadFile(){};


    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public boolean isGoogleNet() {
        return googleNet;
    }

    public void setGoogleNet(boolean googleNet) {
        this.googleNet = googleNet;
    }

    public boolean isVggNet() {
        return vggNet;
    }

    public void setVggNet(boolean vggNet) {
        this.vggNet = vggNet;
    }

    public boolean isResNet() {
        return resNet;
    }

    public void setResNet(boolean resNet) {
        this.resNet = resNet;
    }

    public boolean isSelectAll() {
        return selectAll;
    }

    public void setSelectAll(boolean selectAll) {
        this.selectAll = selectAll;
    }
}
