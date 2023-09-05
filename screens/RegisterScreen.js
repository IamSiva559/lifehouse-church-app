import { Button, StyleSheet, Text, TextInput, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const RegisterScreen = ({ navigation, setUser }) => {
  return (
    <View style={styles.screen}>
      <TextInput placeholder="Name" />
      <TextInput placeholder="Mobile" />
      <TextInput placeholder="Email" />
      <TextInput placeholder="Date of Birth" />
      <TextInput placeholder="Gender" />
      <TextInput placeholder="Password" />
      <TextInput placeholder="Confirm Password" />
      <Button title="Register" onPress={() => setUser({})} />
      <Button title="Login" onPress={() => navigation.replace("Login")} />
    </View>
  );
};

export default RegisterScreen;

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});
