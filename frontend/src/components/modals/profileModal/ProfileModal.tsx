import { useContext, useState } from "react";
import { WebSocketContext } from "../../../contexts/webSocketContext";
import ProfileEditor from "../../profileEditor/ProfileEditor";
import Modal from "../../modal/Modal";

const ProfileModal = ({
  isOpen,
  setIsOpen,
  header,
  onSave,
  onDelete,
  data,
  content,
  setContent,
}: any) => {
  const wsContext = useContext(WebSocketContext);
  const settings: any = wsContext?.data?.settings
  ? Object.keys(wsContext?.data?.settings).reduce((acc, id) => {
      acc[id] = wsContext?.data?.settings[id].value;
      return acc;
    }, {})
  : {};
  const codecs: any = wsContext?.data?.codecs;
  const containers: any = wsContext?.data?.containers;
  const encoders: any = wsContext?.data?.encoders;
  const [tabSelected, setTabSelected] = useState("summary");
  const onClose = () => {
    setIsOpen(false);
  };
  if (!isOpen) return null;
  return (
    <Modal
      isOpen={isOpen}
      setIsOpen={setIsOpen}
      title={header}
      onClose={onClose}
      onSave={onSave}
      showDelete={data?.id != settings?.defaultProfile}
      onDelete={onDelete}
    >
      <ProfileEditor
        content={content}
        setContent={setContent}
        tabSelected={tabSelected}
        setTabSelected={setTabSelected}
        containers={containers}
        encoders={encoders}
        codecs={codecs}
      />
    </Modal>
  );
};
export default ProfileModal;
