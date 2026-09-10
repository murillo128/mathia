# MI-011 — Initial and positive-heat transition visibility obey different outward barriers in the maximal-contact control

**Evidence level:** exact state-identification barriers, corrected fundamental-domain initial threshold, near-antipodal future control, and positive-heat edge-mode exposure through XF-155

## Core intuition

Exact state identification is much easier than stable recovery of the de Bruijn--Newman transition parameter, but there is not one universal complex-reach threshold for every future heat time. The maximal-contact matched family has a sharp **initial** outward visibility boundary, while positive heat can reveal a different spectral edge mechanism outside the near-antipodal regime.

The target-side obstruction is therefore direction- and observation-mechanism-specific. A source-faithful Xi route must price both complex reach and heat-time spectral selection instead of treating the initial slice as the entire future history.

## Strongest justified principle

XF-143--XF-151 show that polynomially normalized real sensors, finite/infinite derivative jets and shallow complex collars can identify state while remaining exponentially blind to `Lambda_per`. Near the antipode they predict the parabolic depth scale `d^2/L`.

The withdrawn XF-152 is not current evidence. XF-154 replaces its usable content with an exact initial-slice theorem on the physical fundamental domain `0<=D<=pi/2`. The outward rate `F_+(H,D)=H+(1/2)log(cos^2 D+sinh^2 H)` has a unique threshold `H_*(D)` for `D>0`, with `H_*(0)=0` and near-antipodal physical expansion `h_*(d)=(pi/2)d^2/L-(pi^3/24)d^4/L^3+...`.

XF-153 controls optimization over positive heat only in its near-antipodal sector, where future evolution changes the signal by at most a constant factor and preserves the initial exponential boundary. XF-155 finds a separate global lower bound on future visibility: choosing `u_N=c log N/N`, `c>2`, isolates the outward highest-frequency edge mode with rate `2H-log 2` uniformly in `D`. Hence the full future cannot remain exponentially blind for `H>(1/2)log 2`, even when the initial slice at that point is still below its own threshold.

## Program consequence

Derive a source-faithful Xi observation theorem that states explicitly which mechanism is used: initial outward continuation, near-antipodal future history, or positive-heat edge-mode selection. Prove controlled normalization and an inverse modulus in that channel, or derive Xi-specific source constraints excluding the matched packet. Do not extrapolate the near-antipodal XF-153 bound into a global all-future statement.

## Counterevidence / boundary

XF-155 gives an upper cap on any hidden full-future region, not an exact full-future threshold below `H=(1/2)log 2`. XF-154 is an initial-slice result; XF-153 remains valid only in its stated sector. None of these findings proves that Xi realizes the matched packet or that crossing a visibility barrier yields stable recovery.

## Epistemic status

**Exact initial outward threshold plus a distinct positive-heat edge-mode visibility mechanism; the complete full-future boundary and source realizability remain open.**

## Falsification criterion

Invalidate XF-154's fundamental-domain initial rate/threshold, the sector assumptions of XF-153, or XF-155's edge-mode asymptotic. A positive continuation should derive the actual source-conditioned observation class and determine which barrier controls it.
