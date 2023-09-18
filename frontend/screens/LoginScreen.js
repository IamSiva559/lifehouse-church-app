import { Button, StyleSheet, Text, TextInput, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const LoginScreen = ({ navigation, setUser }) => {
  return (
    <View style={styles.screen}>
      <TextInput placeholder="Mobile" />
      <TextInput placeholder="Password" />
      <TextInput />
      <Button
        title="Login"
        onPress={() =>
          setUser({
            id: 12345,
            name: "Jeffrey Rujen",
            mobile: 9043843538,
            email: "jeffrey.rujen@gmail.com",
            dateOfBirth: "15/09/2000",
            age: 22,
            gender: "Male",
            address:
              "006 A block, Sai Sunshine Apartment, Munnekollal, Bangalore - 560037",
            currentStage: "Foundation 101",
            interactionStartDate: "",
            inviteDate: "",
            followUpStartDate: "",
            plantedDate: "",
            baptized: true,
            connectGroupLeader: "Ps Michael Praveen",
            connectGroupPTL: "",
            connectGroupRole: "PTL",
            ministryTeam: "Videography",
            ministryTeamLeader: "Preethi",
            ministryTeamRole: "Trainer (streaming)",
            // TODO: Foundation 101, Alpha, Bible Study
            // TODO: 5 developmental tracks
          })
        }
      />
      <Button title="Register" onPress={() => navigation.replace("Register")} />
    </View>
  );
};

export default LoginScreen;

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});
