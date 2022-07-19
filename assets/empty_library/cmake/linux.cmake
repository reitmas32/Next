#   cmake/linux.cmake

########################
#     Main Dirs of     #
#       Project        #
########################
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include ${INCLUDE_EXTERN} ${INCLUDE_LOCAL})
set(BUILD_DIR ${CMAKE_CURRENT_SOURCE_DIR}/build)

#Add Dependencies
include(cmake/vendor.cmake)

########################
#    Include Dirs of   #
#       Project        #
########################
include_directories(
    .
    ${INCLUDE_DIR}
    ${INCLUDE_LIBS}
    #Includes of libraries
)

########################
#    Find Source of    #
#       Project        #
########################
file( GLOB_RECURSE LIB_SOURCES ${SOURCE_DIR}/*.cpp )
file( GLOB_RECURSE LIB_HEADERS ${INCLUDE_DIR}/*.hpp )

if( static_library AND static_library STREQUAL "on")

    ########################
    #     Add Source of    #
    #    Static Library    #
    ########################
    add_library(
        ${APP} STATIC
        ${LIB_SOURCES} 
        ${LIB_HEADERS}
    )

elseif(dynamic_library AND dynamic_library STREQUAL "on")

    ########################
    #     Add Source of    #
    #   Dynamic Library    #
    ########################
    add_library(
        ${APP} SHARED
        ${LIB_SOURCES} 
        ${LIB_HEADERS}
    )

elseif(executable AND executable STREQUAL "on")

    ########################
    #     Add Source of    #
    #       Project        #
    ########################
    #TODO: add_library
    add_executable(
        ${APP} 
        ${LIB_SOURCES} 
        ${LIB_HEADERS}
    )
endif()


target_link_libraries(${APP}
    #ibraries
    ${LIBS}
    ${EXTERN_LIBS}
)