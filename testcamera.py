# import phoXi
import logging # importing logging module
import keyboard  # Library for detecting keypresses
from phoXi import PhoXiControl, PhoXiError, Frame # importing PhoXiControl and Frame classes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def capture_image(phoXi_device): # defining capture_image function
    """Function to capture an image and process the point cloud."""
    logging.info("Capturing image...")
    frame = Frame() # setting up frame
    try:
        phoXi_device.TriggerFrame(frame) # capturing image
    except PhoXiError as e: # exception handling
        logging.error(f"Error capturing image: {e}")
        return

    if frame:  # checking whether the frame is captured or not.
        logging.info("Image captured successfully.")

        # Access point cloud data from the captured frame
        point_cloud = frame.GetPointCloud() # assigning point cloud to a variable containing point cloud data
        logging.info(f"Point cloud has {len(point_cloud)} points.") # logging has the length number of points in the point cloud

        # Example: Save point cloud to a PLY file
        save_path = "captured_point_cloud.ply"  # full file path with file extension # saving point cloud to a PLY file
        success = frame.SaveAsPLY(save_path)
        if success:  # if the point cloud is saved
            logging.info(f"Point cloud saved to {save_path}.") # logging that the point cloud is saved
        else:
            logging.error("Failed to save point cloud.")
    else:
        logging.error("Failed to capture image.")


# Defining main function to run the program
def main(): # defining main function
    try:
        # Initialize the PhoXi Control Interface
        phoXi = PhoXiControl() # set up phoXi
        logging.info("PhoXi Control Interface initialized.") # logging that PhoXi Control Interface is initialized

        # Get a list of available devices
        devices = phoXi.GetDeviceList()

        if not devices:  # if devices is not found
            logging.error("No PhoXi device found.")
            return

        # List available devices
        logging.info("Available PhoXi devices:")
        for idx, device in enumerate(devices): # checking for available devices
            logging.info(f"Device {idx}: {device.HWIdentification}, Type: {device.Type}") # if found list them having Device ID and Type

        # User selects a device
        if len(devices) > 1: # checking if devices are more than 1
            selected_index = int(input(f"Select device (0-{len(devices)-1}): ")) # set selected index to input
            if selected_index < 0 or selected_index >= len(devices): #  checking if selected index is valid
                logging.error("Invalid device index selected.") # set error
                return
            device = devices[selected_index] # set device to selected index
        else:
            device = devices[0]

        logging.info(f"Connecting to device {device.HWIdentification}...")

        # Connect to the selected device
        phoXi_device = phoXi.CreateAndConnect(device.HWIdentification)

        if not phoXi_device: # checking if device is connected or not
            logging.error("Failed to connect to the device.") # set error
            return

        logging.info("Device connected successfully.") # logging that device is connected

        # Stop any existing acquisition
        if phoXi_device.isAcquiring(): # checking if device is acquiring
            phoXi_device.StopAcquisition() # stop acquisition
            logging.info("Existing acquisition stopped.")

        # Set trigger mode to software
        phoXi_device.TriggerMode = "Software" # setting trigger mode as software
        logging.info("Trigger mode set to Software.") # logging that trigger mode is set to software

        # Start acquisition
        phoXi_device.StartAcquisition() # starting acquisition
        logging.info("Acquisition started.") # logging that acquisition is started

        # Main loop to wait for key presses
        try:
            while True: # set while loop
                if keyboard.is_pressed('t'):  # Trigger capture on 't' key press
                    logging.info("'t' key pressed. Triggering camera...") # logging that camera is triggered
                    capture_image(phoXi_device) # calling capture_image function and capturing image

                if keyboard.is_pressed('q'):  # Quit loop on 'q' key press
                    logging.info("'q' key pressed. Exiting...")
                    break
        except KeyboardInterrupt: # exception handling
            logging.info("Ctrl+C pressed. Exiting...")
        finally:
            # Stop acquisition and disconnect device if connected
            if 'phoXi_device' in locals():  # checking if the phoXi_device is in the locals()
                if phoXi_device.isAcquiring(): # if device is acquiring
                    phoXi_device.StopAcquisition() # stop acquisition
                    logging.info("Acquisition stopped.") # logging that acquisition is stopped
                phoXi_device.Disconnect()  # if not disconnect the device
                logging.info("Device disconnected.")
    except PhoXiError as e: # exception handling
        logging.error(f"Error during program execution: {e}")


if __name__ == "__main__": # if __name__ is main
    main() # calling main function

