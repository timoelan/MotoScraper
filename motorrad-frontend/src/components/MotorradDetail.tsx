import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getTuttiContent } from '../services/api';
import { Typography, Button, Container, Box } from '@mui/material';

interface Motorrad {
  id: string;
  Titel: string;
  Link: string;
  Beschreibung: string;
  Preis: string;
  Ort: string;
  "Bild-URL": string;
}

const MotorradDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>(); 
  const [motorrad, setMotorrad] = useState<Motorrad | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const tuttiContent = await getTuttiContent();
        console.log("Tutti Content:", tuttiContent[0]); 
        const selectedMotorrad = tuttiContent.find((m: Motorrad) => m.id.toString() === id);
        console.log("teststst",selectedMotorrad, id)
        setMotorrad(selectedMotorrad || null);
      } catch (error) {
        console.error("Fehler beim Abrufen der Daten:", error);
      }
    };
  
    fetchData();
  }, [id]);

  if (!motorrad) {
    return <Typography>Lade...</Typography>;
  }

  return (
    <Container style={{ marginTop: '2rem' }}>
      <Box display="flex" flexDirection={{ xs: 'column', md: 'row' }} gap={4}>
        <Box flex={1}>
          <img
            src={motorrad["Bild-URL"]}
            alt={motorrad.Titel}
            style={{ width: '100%', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0, 0, 0, 0.1)' }}
          />
        </Box>
        <Box flex={2}>
          <Typography variant="h3" gutterBottom>
            {motorrad.Titel}
          </Typography>
          <Typography variant="h4" color="primary" gutterBottom>
            {motorrad.Preis}
          </Typography>
          <Typography variant="body1" gutterBottom>
            <strong>Ort:</strong> {motorrad.Ort}
          </Typography>
          <Typography variant="body1" gutterBottom>
            <strong>Beschreibung:</strong> {motorrad.Beschreibung}
          </Typography>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => window.open(motorrad.Link, '_blank')}
            style={{ marginTop: '1rem' }}
          >
            Zum Inserat
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default MotorradDetail;