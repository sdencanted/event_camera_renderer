// -*-c++-*---------------------------------------------------------------------------------------
// Copyright 2022 Bernd Pfrommer <bernd.pfrommer@gmail.com>
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef EVENT_CAMERA_RENDERER__RENDERER_ROS1_H_
#define EVENT_CAMERA_RENDERER__RENDERER_ROS1_H_

#include <event_camera_codecs/decoder.h>
#include <event_camera_codecs/decoder_f actory.h>
#include <event_camera_msgs/EventPacket.h>
#include <image_transport/image_transport.h>
#include <ros/ros.h>
#include <sensor_msgs/Image.h>

#include <memory>
#include <string>

#include "event_camera_renderer/display.h"

namespace event_camera_renderer
{
class Renderer
{
public:
  using MagEventPacket = event_camera_msgs::MagEventPacket;
  explicit Renderer(ros::NodeHandle & nh);
  ~Renderer();

private:
  void frameTimerExpired(const ros::TimerEvent &);
  void eventMsg(const MagEventPacket::ConstPtr & msg);
  void imageConnectCallback(const image_transport::SingleSubscriberPublisher &);
  void startNewImage();

  // ------------------------  variables ------------------------------
  ros::NodeHandle nh_;
  std::shared_ptr<Display> display_;
  ros::Timer frameTimer_;     // fires once per frame
  double sliceTime_;          // duration of one frame
  ros::Subscriber eventSub_;  // subscribes to events
  bool isSubscribedToEvents_{false};
  image_transport::Publisher imagePub_;
  sensor_msgs::Image imageMsgTemplate_;
};
}  // namespace event_camera_renderer
#endif  // EVENT_CAMERA_RENDERER__RENDERER_ROS1_H_
