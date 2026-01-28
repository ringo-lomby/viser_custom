from __future__ import annotations

HUD_HTML = """
<style>
	.unified-hud {
		position: fixed;
		top: 20px;
		left: 50%;
		transform: translateX(-50%);
		width: 90%; /* Increased width */
		max-width: 1200px; /* Increased max-width */
		background-color: rgba(255, 255, 255, 0.03);
		border-radius: 10px;
		color: #FFFFFF;
		font-family: 'Chakra Petch', sans-serif;
		font-weight: bold;
		z-index: 999990;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 15px; /* Increased padding */
		backdrop-filter: blur(10px); /* Increased blur for stronger glass effect */
		border: 1px solid rgba(255, 255, 255, 0.4); /* Subtle white border for reflection */
		transition: opacity 0.2s ease-in-out; /* Added for smoother transitions */

	}
	.hud-main-content {
		display: flex;
		justify-content: space-around;
		align-items: center;
		width: 100%;
	}
	.hud-item {
		display: flex;
        flex-direction: column;
        align-items: center;
	}
	.speed-gauge {
		position: relative;
		width: 150px;
		height: 150px;
	}
	.speed-value {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		font-size: 80px;
	}
	.speed-unit {
		font-size: 16px;
	}
	.battery-bar-container {
		width: 150px;
		height: 20px;
		background-color: #333;
		border-radius: 5px;
		overflow: hidden;
	}
	.battery-bar-fill {
		height: 100%;
		border-radius: 5px;
	}
	.battery-value {
		font-size: 48px;
	}
	.battery-label {
		font-size: 36px;
	}
	.mission-info {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.mission-label {
		font-size: 24px;
		margin-bottom: 5px;
	}
	.mission-data {
		font-size: 35px;
	}
	.mission-unit {
		font-size: 16px; /* Smaller font size for units */
	}
	.traffic-light {
		width: 100px;
		height: 100px;
		border-radius: 50%;
		border: 2px solid #FFFFFF;
	}
	.notification {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 15px 10px 10px 10px; /* Adjusted padding for top border */
		border-radius: 5px;
		color: #FFFFFF;
		background-color: transparent;
		margin-top: 0; /* No margin-top needed if padding handles spacing */
		min-height: 75px;
		width: 100%;
		border-top: 1px solid rgba(255, 255, 255, 0.2); /* Divider on top */
	}
	.notification-msg {
		font-size: 20px;
		text-align: left;
	}
	.notification-content {
		display: flex;
		justify-content: space-between;
		width: 100%;
		gap: 20px;
	}
	.notification-content .column-left {
		flex: 1;
		text-align: left;
		border-right: 1px solid rgba(255, 255, 255, 0.2); /* Divider between columns */
		padding-right: 10px; /* Space before the divider */
	}
	.notification-content .column-right {
		flex: 1;
		text-align: left;
		padding-left: 10px; /* Space after the divider */
	}
	.column-label {
		font-size: 0.8em; /* Slightly smaller font size */
		font-weight: bold;
		opacity: 0.7; /* Slightly faded */
		margin-bottom: 5px; /* Space below the label */
		display: block; /* Ensures it takes up its own line */
	}
</style>
"""
