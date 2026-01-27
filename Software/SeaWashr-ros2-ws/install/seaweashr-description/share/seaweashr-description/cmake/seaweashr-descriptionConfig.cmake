# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_seaweashr-description_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED seaweashr-description_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(seaweashr-description_FOUND FALSE)
  elseif(NOT seaweashr-description_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(seaweashr-description_FOUND FALSE)
  endif()
  return()
endif()
set(_seaweashr-description_CONFIG_INCLUDED TRUE)

# output package information
if(NOT seaweashr-description_FIND_QUIETLY)
  message(STATUS "Found seaweashr-description: 0.0.0 (${seaweashr-description_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'seaweashr-description' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT seaweashr-description_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(seaweashr-description_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${seaweashr-description_DIR}/${_extra}")
endforeach()
