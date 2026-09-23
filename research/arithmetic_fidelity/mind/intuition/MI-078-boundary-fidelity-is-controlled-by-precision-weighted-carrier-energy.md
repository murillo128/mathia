# MI-078 — Boundary fidelity is controlled by precision-weighted carrier energy

**Evidence level:** supported by the boundary-conditioning synthesis in [AF-529](../../findings/AF-529-finite-boundary-secants-quantify-log-slope-conditioning.md), [AF-530](../../findings/AF-530-full-boundary-shape-has-sharp-minimax-conditioning-scale.md), [AF-531](../../findings/AF-531-independent-gaussian-sampling-has-sharp-inverse-square-profile-recovery-threshold.md), and [AF-532](../../findings/AF-532-correlated-gaussian-boundary-profiles-are-governed-by-precision-weighted-carrier-energy.md).

For the simple-source boundary family, the physical carrier scale is

`delta_A = log A/(A log log A)`.

AF-529 shows that one finite boundary secant already exposes the log-slope parameter only at this scale: adversarial error `o(delta_A)` preserves order-one parameter separation, while error of order `delta_A` can mask it. AF-530 then shows that observing the entire anchored boundary profile does not improve that minimax scale. After normalization the profile is asymptotically rank one,

`F_(A,theta)(u) = delta_A (u(1-theta)+o(1))`,

so dense sampling of the same shape is not automatically new information.

AF-531 and AF-532 identify the quantity that does measure new information once a stochastic noise geometry is specified. For independent Gaussian samples the effective signal is

`S_A^2 = (delta_A^2/sigma_A^2) sum_i u_i^2`,

while for correlated Gaussian noise it is the precision-weighted carrier energy

`J_A = delta_A^2 u_A^T Sigma_A^(-1) u_A`.

The recovery threshold is `J_A -> infinity`; bounded `J_A` leaves a nondegenerate Gaussian location experiment, and `J_A -> 0` makes distinct order-one parameters asymptotically indistinguishable. Independent repeated samples help only because they increase this quadratic energy. Correlated repetition can saturate, while a spread design can recover the inverse-square sampling gain when it adds genuinely new precision in the carrier direction.

The durable lesson is that sample count, profile density, and nominal resolution are only proxies. For a low-rank physical signal, fidelity is controlled by how much inverse-noise geometry lies along the source-sensitive carrier. More observations help only to the extent that they increase that precision-weighted energy.

**Boundary.** These findings concern the stated simple-source boundary experiment and Gaussian/adversarial observation models. They do not establish a universal information criterion for nonlinear source families, non-Gaussian noise, or source identification beyond the one-parameter boundary model.