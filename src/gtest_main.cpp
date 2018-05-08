//
// Created by Jakub Hazik on 5/1/18.
//

#include <gtest/gtest.h>
#include <ros/ros.h>

//// Run all the tests that were declared with TEST()
GTEST_API_ int main(int argc, char **argv) {
    ros::init(argc, argv, "phoxi_camera_node_unittest");
    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}