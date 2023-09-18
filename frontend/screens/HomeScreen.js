import { Button, Pressable, StyleSheet, Text, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const HomeScreen = ({ userData, navigation }) => {
  return (
    <View style={styles.screen}>
      <Pressable
        style={styles.section}
        onPress={() => navigation.navigate("ConnectGroup")}
      >
        <Text>Connect Group</Text>
        <Text>Leader - {userData.connectGroupLeader}</Text>
        {userData.connectGroupPTL !== "" ? (
          <Text>PTL - {userData.connectGroupPTL}</Text>
        ) : null}
        <Text>Role - {userData.connectGroupRole}</Text>
      </Pressable>
      <Pressable
        style={styles.section}
        onPress={() => navigation.navigate("MinistryTeam")}
      >
        <Text>Ministry Team - {userData.ministryTeam}</Text>
        <Text>Leader - {userData.ministryTeamLeader}</Text>
        <Text>Role - {userData.ministryTeamRole}</Text>
      </Pressable>
      <View style={styles.section}>
        <Text>Current Stage</Text>
        <Text>{userData.currentStage}</Text>
        <Button
          title="Profile"
          onPress={() => navigation.navigate("Profile")}
        />
        <Button
          title="Settings"
          onPress={() => navigation.navigate("Settings")}
        />
      </View>
    </View>
  );
};

export default HomeScreen;

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    alignItems: "center",
    justifyContent: "space-evenly",
  },
  section: {
    alignItems: "flex-start",
    justifyContent: "space-evenly",
    backgroundColor: "#ddd",
    height: "33%",
    width: "100%",
    paddingLeft: 36,
    borderRadius: 16,
  },
});
