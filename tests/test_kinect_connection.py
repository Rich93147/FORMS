
import cv2 as cv

from kinect_next import KinectSensor as ks, StreamType as st, JointType as jt, draw_all_skeletons as das


# Enable Skeleton tracking and the depth stream
streams = st.BODY | st.DEPTH | st.COLOR

print("Connecting to Kinect...")
print("Press Q or ESC to quit.")

body_detected = False

try:
    # Open the sensnor and automatically release when finished
    with ks(streams=streams) as kinect:
        print("Kinect connected. Finding bodies...")

        for frames in kinect.poll_frames():

            # Display the live RGB camera feed
            if frames.color is not None:
                color_image = frames.color.as_bgr().copy()

                # Draw tracked skeletons over the RGB image
                das(
                    color_image,
                    frames.bodies,
                    kinect.mapper,
                    target_space="color"
                )

                # Resize the image to fit the screen
                color_image = cv.resize(
                    color_image, (960, 540)
                )

                cv.imshow("Kinect RGB + Skeleton", color_image)

            # Display the Kinect depth stream
            if frames.depth is not None:
                depth_image = frames.depth.to_normalized_uint8()

                cv.imshow("Kinect Depth", depth_image)

            # Check if any bodies are being tracked in the current frame
            if frames.tracked_bodies and not body_detected:
                body = frames.tracked_bodies[0]
                body_detected = True

                print(f"\nBody Tracking ID: {body.tracking_id}")
                print(f"Timestamp: {frames.relative_time_ns} ns")
                print("\n3D Joint Coordinates (meters):")

                # Print the 3D coordinates for each joint
                for joint_type in jt:
                    joint = body.joints[joint_type]
                    position = joint.position
                    print(
                        f"{joint_type.name}: "
                        f"X={position.x:.3f}, "
                        f"Y={position.y:.3f}, "
                        f"Z={position.z:.3f}"
                    )

            # Keep the viewer responsive and check for exit keys
            key = cv.waitKey(1) & 0xFF

            if key == ord("q") or key == 27:
                break

finally:
    cv.destroyAllWindows()

if body_detected:
    print("Body detected successfully.")

print("Kinect connection test completed.")
