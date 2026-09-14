# MI-017 — A finite zero edge upgrades Robin recovery to a phase-locked corridor, but the full edge face still realizes the adaptive ray

**Evidence level:** exact consequence of [RE-112](../../findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md), [RE-113](../../findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md), and [RE-114](../../findings/RE-114-actual-finite-edge-zero-face-realizes-the-adaptive-mixed-race-ray-syndetically.md). No contradiction with false RH or density theorem for selected CA blocks is claimed.

Let `Theta=sup Re(rho)`. In the false-RH finite-edge regime `1/2<Theta<1`, RE-112 first replaces the textbook `x^Theta log^2 x` bound by the log-free envelope

`psi(x)-x = O_Theta(x^Theta)`

and transfers it to the full CA event sweep. RE-110 then forces the scalar recovery corridor

`V-Y >>_Theta h(C) Y^(2-Theta) log Y`.

RE-113 shows that the scalar envelope discards decisive phase information. The same high-strip reciprocal summability projects the normalized source onto the actual rightmost zero face:

`x-vartheta(x) = x^Theta(F_Theta(log x)+o(1))`,

where `F_Theta` is an absolutely convergent real almost-periodic sum over zeros with `Re rho=Theta`. The adaptive RE-034 selector locks this phase to the selected Robin height:

`F_Theta(log Y) = b h(C) Y^(1-Theta) log Y + o(1)`.

If the first recovery is genuinely sublinear, `V-Y=o(Y)`, the scalar corridor forces `lambda_Y=h(C)Y^(1-Theta)log Y -> 0`; uniform continuity then makes every crossed event see vanishing edge phase. Hence the forward workload is `o(Y^Theta)`, not merely `O(Y^Theta)`, and

`V-Y = omega(h(C) Y^(2-Theta) log Y)`.

So sublinear selected recoveries cannot saturate the scalar finite-edge minimum. A fixed-constant near-minimal family, if it exists under `V-Y<=Y`, must instead be macroscopic and edge-amplitude:

`h(C) asy Y^(Theta-1)/log Y`, `V-Y asy Y`, and `F_Theta(log Y) asy 1`.

RE-114 tests the most immediate strengthening: combine this Chebyshev edge phase with the reciprocal-Mertens coordinate already selected by RE-034. It derives a second actual-edge profile

`G_Theta(u)=sum_(Re rho=Theta) exp(i Im(rho)u)/(1-rho)`

and the joint selector lock

`F_Theta(log Y)=b lambda_Y+o(1)`,

`G_Theta(log Y)=(1-b)lambda_Y+o(1)`.

The corresponding ray residual `K_(Theta,b)=bG_Theta-(1-b)F_Theta` is not coercive. Writing the exponentially stable filter `J_Theta` with `G_Theta=J_Theta-F_Theta`, one gets

`K_(Theta,b)=J_Theta' + (b-(1-Theta))J_Theta`.

Uniform almost-periodicity of the absolutely convergent actual edge face then forces exact sign-correct ray phases to occur **syndetically**: every sufficiently late logarithmic interval of bounded length contains a phase where `K_(Theta,b)=0` and both `F_Theta` and `G_Theta` are bounded below positively. Thus adding the reciprocal coordinate sharpens the selector dictionary but does not by itself obstruct the attained-edge branch.

The live finite-edge problem is now **selector placement relative to syndetic compatibility windows**, or a source coordinate beyond the leading edge face. A closing theorem must show that the CA selector cannot repeatedly land in those bounded-gap edge-ray windows, exploit a lower-order term at finer resolution, or couple recovery geometry to selector placement in a way the almost-periodic edge model does not preserve.

The reusable split is sharper. If the finite edge is not attained, RE-113 already excludes unbounded fixed-constant near-minimal recovery. If it is attained, RE-114 shows that the full leading edge spectrum itself supplies compatible order-one mixed Chebyshev/Mertens phases with bounded logarithmic gaps. The extreme `Theta=1` branch remains the separate unconditional RE-109--RE-111 problem.

**Boundary.** Almost-periodicity and the standard/reciprocal explicit-formula coefficients are classical. The durable Mathia content is the selector-conditioned edge projection, the sublinear anti-saturation law, and the fact that the complete attained edge face still realizes the adaptive mixed ray syndetically. None of this proves that actual CA selectors hit those phases.