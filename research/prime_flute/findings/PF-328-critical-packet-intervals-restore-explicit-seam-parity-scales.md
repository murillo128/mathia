# PF-328 — critical packet intervals restore the explicit seam parity scales

**Status:** `EXACT-DERIVED + UNIFORM-CRITICAL-INTERVAL + SEAM-SCALE-RESTORATION + ROUTE-NARROWING`.

PF-325 turns the local Hilbert--Schmidt endpoint into an exact integral over the physical center `t` of the normalized low-packet orbit. PF-326 identifies the exact fixed-band seam pullback in the two face-parity channels, and PF-327 proves that, after raw-`L^2` shape normalization, a packet centered at one PF-323 critical point still has order-one compactified transverse energy. Two gaps remain between those statements and the live endpoint test:

1. PF-327 is stated at one fixed critical level `lambda`, whereas PF-325 measures a **set of packet centers**;
2. PF-327 deliberately divides out the common parity-dependent seam factor, whereas the actual PF-325 packet is unit in the seam-energy Hilbert space and therefore carries that factor.

Both gaps can be closed exactly before any one-cusp-pant calculation.

Fix

\[
0<\lambda_0<\lambda_1<1,
\qquad
0<R<\log(1/\lambda_1),
\]

and let

\[
\tau_{n,\lambda}=\operatorname{arcosh}(\lambda/s_n)
\]

be the PF-323 critical center. The whole center interval

\[
I_n=[\tau_{n,\lambda_0},\tau_{n,\lambda_1}]
\]

has the nonzero limiting physical length

\[
\boxed{|I_n|\longrightarrow\log(\lambda_1/\lambda_0).}
\]

For every center in this interval, the PF-327 critical-energy limit is uniform in `lambda`. Thus the shape-normalized seam pullbacks are not critical only at an isolated packet position: they occupy a positive-measure interval in the **same translation parameter used by PF-325**.

The common seam factors are also explicit. Let `w_n` be the shrinking seam half-width used in PF-326, let `psi_{n,t}^sigma` be PF-325's equal-amplitude unit packet in one exact seam-normalized face-parity channel `sigma in {+,-}`, and put

\[
u_{n,t}^\sigma=\Lambda_{Q,n}^{-1/2}\psi_{n,t}^\sigma,
\qquad
\rho_{n,\sigma}=\|u_{n,t}^\sigma\|_{L^2}.
\]

Translation invariance of the seam makes `rho_{n,sigma}` independent of `t`. PF-326's fixed-band asymptotics imply

\[
\boxed{
w_n\rho_{n,+}^2\longrightarrow
A_\kappa:=\frac{\arctan\kappa}{\kappa}>0,
}
\]

and

\[
\boxed{
w_n^{-1}\rho_{n,-}^2\longrightarrow1.}
\]

Therefore restoring the factor divided out in PF-327 gives an explicit parity asymmetry at the unprojected transverse-form stage: the symmetric seam-energy unit packet carries critical raw transverse energy of order `w_n^{-1}`, while the antisymmetric packet carries order `w_n`. These are **pre-angle energy scales**, not angle lower bounds; the final intrinsic diagonal normalization may absorb them.

More precisely, if

\[
J_{\sigma,R}:=
\int_{-R}^{R}e^{2x}|G_\sigma(x)|^2\,dx>0
\]

for the PF-326 limiting profiles `G_sigma`, then the raw-`L^2` shape-normalized critical energy satisfies

\[
\boxed{
\int_{I_n}
 s_n^2\!
 \int_{|\tau-t|\le R}
 \cosh^2\tau\,|g_{n,t}^\sigma(\tau)|^2\,d\tau\,dt
\longrightarrow
\frac{\lambda_1^2-\lambda_0^2}{2}\,J_{\sigma,R},
}
\]

where `g_{n,t}^sigma=u_{n,t}^sigma/rho_{n,sigma}`. Restoring the actual seam-normalized unit packet gives

\[
\boxed{
 w_n
 \int_{I_n}
 s_n^2\!
 \int_{|\tau-t|\le R}
 \cosh^2\tau\,|u_{n,t}^+(\tau)|^2\,d\tau\,dt
\longrightarrow
A_\kappa\frac{\lambda_1^2-\lambda_0^2}{2}J_{+,R},
}
\]

and

\[
\boxed{
 w_n^{-1}
 \int_{I_n}
 s_n^2\!
 \int_{|\tau-t|\le R}
 \cosh^2\tau\,|u_{n,t}^-(\tau)|^2\,d\tau\,dt
\longrightarrow
\frac{\lambda_1^2-\lambda_0^2}{2}J_{-,R}.
}
\]

PF-233's positive form comparison transfers the corresponding lower scales to the variable-width diagonal corridor before physical `L/H` projection and common pant completion.

This changes how the PF-325 fallback should be falsified. If a completed local angle block `B_{n,r}` really satisfies the PF-318 Hilbert--Schmidt budget, then PF-325 forces

\[
\int_{I_n}\|(B_{n,r})^*\psi_{n,t}\|^2dt
\lesssim\frac{1+\log P_n}{P_n^2}\longrightarrow0.
\]

Consequently, for every fixed `eta>0`,

\[
\boxed{
\left|
\left\{t\in I_n:
\|(B_{n,r})^*\psi_{n,t}\|\ge\eta
\right\}
\right|
\longrightarrow0.
}
\]

The surviving pant-side mechanism must therefore suppress the completed response on **almost all of a positive-length family of compactification-critical packet centers**. Suppression at one distinguished center is not enough, and the critical family cannot be dismissed as a measure-zero exception to the PF-325 position integral.

## Claim

Fix a physical cutoff `kappa>0`, numbers

\[
0<\lambda_0<\lambda_1<1,
\qquad
0<R<\log(1/\lambda_1),
\tag{1}
\]

and one seam face-parity channel `sigma in {+,-}`. Let `s_n`, `ell_n`, and `w_n` be the canonical quantities used by PF-323 and PF-326, and define

\[
\tau_{n,\lambda}=\operatorname{arcosh}(\lambda/s_n),
\qquad
I_n=[\tau_{n,\lambda_0},\tau_{n,\lambda_1}].
\tag{2}
\]

Let

\[
N_n=\left\lfloor\frac{\kappa\ell_n}{2\pi}\right\rfloor,
\qquad m_n=2N_n,
\]

and in the `sigma` parity channel let

\[
\psi_{n,t}^\sigma
=\frac1{\sqrt{m_n}}
\sum_{1\le|k|\le N_n}
e^{-i\xi_{n,k}t}e_{n,k}^\sigma,
\qquad
\xi_{n,k}=\frac{2\pi k}{\ell_n},
\tag{3}
\]

be the equal-amplitude unit packet in the exact seam-normalized low Hilbert coordinates. Put

\[
u_{n,t}^\sigma
:=\Lambda_{Q,n}^{-1/2}\psi_{n,t}^\sigma,
\qquad
\rho_{n,\sigma}:=\|u_{n,t}^\sigma\|_{L^2},
\qquad
g_{n,t}^\sigma:=\rho_{n,\sigma}^{-1}u_{n,t}^\sigma.
\tag{4}
\]

Then:

1. the critical-center interval has a positive fixed limit,
   \[
   \boxed{
   |I_n|\to\log(\lambda_1/\lambda_0)>0;
   }
   \tag{5}
   \]
2. the exact seam pullback norm is independent of `t` and obeys
   \[
   \boxed{
   w_n\rho_{n,+}^2\to A_\kappa
   :=\frac{\arctan\kappa}{\kappa},
   \qquad
   w_n^{-1}\rho_{n,-}^2\to1;
   }
   \tag{6}
   \]
3. with the PF-326 limiting profiles
   \[
   G_\sigma(x)
   =\frac1{\sqrt{2\pi S_\sigma}}
   \int_{-\kappa}^{\kappa}
   b_\sigma(\xi)e^{i\xi x}\,d\xi,
   \tag{7}
   \]
   where
   \[
   b_+(\xi)=(1+\xi^2)^{-1/2},
   \qquad b_-(\xi)=1,
   \tag{8}
   \]
   and
   \[
   J_{\sigma,R}:=
   \int_{-R}^{R}e^{2x}|G_\sigma(x)|^2dx>0,
   \tag{9}
   \]
   one has
   \[
   \boxed{
   \int_{I_n}
   E_{n,\sigma}(t)dt
   \to
   \frac{\lambda_1^2-\lambda_0^2}{2}
   J_{\sigma,R},
   }
   \tag{10}
   \]
   for
   \[
   E_{n,\sigma}(t)
   :=s_n^2
   \int_{|\tau-t|\le R}
   \cosh^2\tau\,
   |g_{n,t}^\sigma(\tau)|^2d\tau;
   \tag{11}
   \]
4. restoring the actual seam-normalized unit packets yields
   \[
   \boxed{
   w_n\int_{I_n}
   \rho_{n,+}^2E_{n,+}(t)dt
   \to
   A_\kappa
   \frac{\lambda_1^2-\lambda_0^2}{2}J_{+,R},
   }
   \tag{12}
   \]
   and
   \[
   \boxed{
   w_n^{-1}\int_{I_n}
   \rho_{n,-}^2E_{n,-}(t)dt
   \to
   \frac{\lambda_1^2-\lambda_0^2}{2}J_{-,R};
   }
   \tag{13}
   \]
5. the same right-hand sides, multiplied by the uniform PF-233 constant `c_0>0`, are lower bounds for the corresponding integrated canonical variable-width diagonal-corridor energies;
6. if a local completed angle block `B_{n,r}` acting on this normalized low packet orbit satisfies PF-318's endpoint budget, then for every fixed `eta>0`,
   \[
   \boxed{
   \left|
   \{t\in I_n:\|(B_{n,r})^*\psi_{n,t}^\sigma\|\ge\eta\}
   \right|
   \le
   \frac{C(1+\log P_n)}{\eta^2P_n^2}
   \to0.
   }
   \tag{14}
   \]

Thus the pre-pant critical family occupies positive measure in the exact PF-325 translation variable, while endpoint closure requires its **completed** response to vanish in measure on that same interval.

## 1. The critical centers fill a fixed physical interval

PF-323 defines

\[
\tau_{n,\lambda}=\operatorname{arcosh}(\lambda/s_n).
\]

For every fixed `lambda>0`, as `s_n->0`,

\[
\operatorname{arcosh}(\lambda/s_n)
=\log\frac{2\lambda}{s_n}+O_{\lambda}(s_n^2).
\tag{15}
\]

Uniformly for `lambda in [lambda_0,lambda_1]`, the error is `O(s_n^2/lambda_0^2)`. Hence

\[
|I_n|
=\tau_{n,\lambda_1}-\tau_{n,\lambda_0}
=\log\frac{\lambda_1}{\lambda_0}+o(1),
\]

which proves (5).

The restriction on `R` is uniform as well. PF-323 proves

\[
\frac{\ell_n}{2}-\tau_{n,\lambda}
>\log(1/\lambda).
\]

For `lambda<=lambda_1`, every radius `R<log(1/lambda_1)` therefore stays strictly inside the cell for all sufficiently large `n`. The left edge also stays interior because `tau_{n,lambda_0}->infinity`.

So the family in (2) is not obtained by moving the PF-327 packet through a region where its local model ceases to apply. One fixed window size works for the entire center interval.

## 2. Restoring the common seam scale is a fixed-band Riemann sum

PF-326 gives the exact hyperbolic-seam parity eigenvalue asymptotics, uniformly for `|xi|<=kappa`,

\[
w_n^{1/2}q_{n,+}(\xi)^{-1/2}
=(1+\xi^2)^{-1/2}(1+O_\kappa(w_n^2)),
\tag{16}
\]

and

\[
w_n^{-1/2}q_{n,-}(\xi)^{-1/2}
=1+O_\kappa(w_n^2).
\tag{17}
\]

Because `Lambda_Q^{-1/2}` is a tangential Fourier multiplier, translation changes only phases and therefore

\[
\rho_{n,\sigma}^2
=\frac1{m_n}
\sum_{1\le|k|\le N_n}
q_{n,\sigma}(\xi_{n,k})^{-1}.
\tag{18}
\]

For the symmetric channel, (16) gives

\[
w_n\rho_{n,+}^2
=\frac1{m_n}
\sum_{1\le|k|\le N_n}
\frac1{1+\xi_{n,k}^2}
+o(1).
\tag{19}
\]

The frequency mesh is `2pi/ell_n`, `N_n~kappa ell_n/(2pi)`, and omission of the zero sample is negligible. Thus

\[
\frac1{m_n}\sum_{1\le|k|\le N_n}
\frac1{1+\xi_{n,k}^2}
\longrightarrow
\frac1{2\kappa}
\int_{-\kappa}^{\kappa}\frac{d\xi}{1+\xi^2}
=\frac{\arctan\kappa}{\kappa}.
\tag{20}
\]

The antisymmetric calculation from (17) is even simpler:

\[
w_n^{-1}\rho_{n,-}^2
=\frac1{m_n}
\sum_{1\le|k|\le N_n}(1+o(1))
\longrightarrow1.
\tag{21}
\]

This proves (6). No identification between the two small quantities `w_n` and `s_n` is used. They play different geometric roles and must remain separate.

## 3. PF-327 is uniform on a compact interval of critical levels

Write a center `t in I_n` uniquely as

\[
t=\tau_{n,\lambda},
\qquad \lambda\in[\lambda_0,\lambda_1].
\]

Translation invariance of the seam pullback means that in the local coordinate `x=tau-t`, the raw-`L^2` normalized shape `g_{n,t}^sigma(t+x)` is independent of the center except for periodic placement. PF-326 therefore gives the same local `L^2([-R,R])` limit `G_sigma` uniformly over this family.

The compactification coefficient has the exact PF-323 identity

\[
s_n\cosh(\tau_{n,\lambda}+x)
=\lambda\cosh x
+\sqrt{\lambda^2-s_n^2}\,\sinh x.
\tag{22}
\]

Since `lambda>=lambda_0>0`, the square root converges to `lambda` uniformly for `lambda in [lambda_0,lambda_1]`. Hence

\[
s_n^2\cosh^2(\tau_{n,\lambda}+x)
\longrightarrow\lambda^2e^{2x}
\tag{23}
\]

uniformly on the product

\[
[\lambda_0,\lambda_1]\times[-R,R].
\]

The same `L^2`-to-`L^1` argument used in PF-327 now gives the uniform limit

\[
\boxed{
E_{n,\sigma}(\tau_{n,\lambda})
\longrightarrow
\lambda^2J_{\sigma,R}
}
\tag{24}
\]

for `lambda in [lambda_0,lambda_1]`.

The limit is uniformly bounded below by `lambda_0^2J_{sigma,R}>0`. Thus even before integrating, every center in `I_n` is a compactification-critical shape witness for all sufficiently large `n`.

## 4. Integrating over the exact PF-325 center variable gives a nonzero limit

Differentiate the defining center:

\[
\frac{d\tau_{n,\lambda}}{d\lambda}
=\frac1{\sqrt{\lambda^2-s_n^2}}.
\tag{25}
\]

Therefore

\[
\int_{I_n}E_{n,\sigma}(t)dt
=
\int_{\lambda_0}^{\lambda_1}
\frac{E_{n,\sigma}(\tau_{n,\lambda})}
{\sqrt{\lambda^2-s_n^2}}d\lambda.
\tag{26}
\]

Equations (24)--(25) converge uniformly on the compact lambda interval, so dominated convergence gives

\[
\begin{aligned}
\int_{I_n}E_{n,\sigma}(t)dt
&\longrightarrow
J_{\sigma,R}
\int_{\lambda_0}^{\lambda_1}\lambda\,d\lambda\\
&=
\frac{\lambda_1^2-\lambda_0^2}{2}J_{\sigma,R},
\end{aligned}
\]

which is (10).

Because `u_{n,t}^sigma=rho_{n,sigma}g_{n,t}^sigma` and `rho_{n,sigma}` is independent of `t`, equations (6) and (10) immediately give (12)--(13). This is exactly the common scalar that PF-327 intentionally removed.

The conclusion is stronger than saying that many individual fixed `lambda` values are critical. It places the whole family directly in PF-325's integration measure and computes its limiting pre-pant mass.

## 5. The variable-width diagonal corridor inherits the same interval lower scale

PF-323's compactified `A` form has a nonnegative derivative term, so `E_{n,sigma}(t)` is a lower bound for the full scaled `A` energy of `g_{n,t}^sigma` on the critical window. PF-233 gives the uniform form comparison

\[
T_{a_n}\ge c_0s_n^2A.
\tag{27}
\]

By homogeneity, applying (27) to `u_{n,t}^sigma=rho_{n,sigma}g_{n,t}^sigma` and integrating over `I_n` gives the lower bounds asserted in item 5, with exactly the same parity scales `w_n^{-1}` and `w_n`.

This remains an **unprojected diagonal-corridor statement**. It proves neither that the symmetric channel blows up nor that the antisymmetric channel disappears in the final angle. The local angle divides by its own completed diagonal energies, and those may carry the same parity scales. The point is narrower and necessary: the common seam factors are now accounted for explicitly rather than being left as an unknown between PF-327 and the pant calculation.

## 6. Endpoint success requires suppression in measure on the critical interval

For the completed local block, PF-325 gives the exact identity

\[
\|B_{n,r}\|_{\mathcal S_2}^2
=\frac{m_n}{\ell_n}
\int_0^{\ell_n}\|(B_{n,r})^*\psi_{n,t}\|^2dt,
\tag{28}
\]

with `m_n/ell_n->kappa/pi>0`. PF-318's endpoint budget therefore implies

\[
\int_0^{\ell_n}\|(B_{n,r})^*\psi_{n,t}\|^2dt
\le C\frac{1+\log P_n}{P_n^2}.
\tag{29}
\]

Restricting to `I_n` only decreases the integral. Chebyshev's inequality then gives

\[
\left|
\{t\in I_n:\|(B_{n,r})^*\psi_{n,t}\|\ge\eta\}
\right|
\le
\eta^{-2}
\int_{I_n}\|(B_{n,r})^*\psi_{n,t}\|^2dt,
\]

which proves (14).

Since `|I_n|->log(lambda_1/lambda_0)>0`, the endpoint has a sharp qualitative consequence: for every fixed response threshold, the fraction of the critical-center interval above that threshold tends to zero. Any proposed positive proof must therefore identify a downstream mechanism that suppresses **almost the whole compactification-critical family**, not one specially selected packet.

Conversely, to falsify the PF-318 route it is now enough to prove a fixed `eta>0` and a fixed positive-measure subset `E_n subset I_n` on which the **completed intrinsic** response stays at least `eta`. PF-325 would then force order-one Hilbert--Schmidt mass, contradicting the required vanishing reciprocal-prime budget.

PF-328 does not prove that final lower bound. It makes the missing bridge measurable and removes two weaker escape routes: isolated-position exceptionalism and an untracked seam-parity scalar.

## Prior-art and novelty audit

No standalone novelty is claimed for the analytic ingredients. The passage from a compact interval of parameters to a uniform asymptotic, Riemann-sum evaluation of fixed-band Fourier multipliers, dominated convergence under the change of variable `t=tau_{n,lambda}`, and Chebyshev's measure inequality are elementary. The translation-orbit identity is the same classical continuous tight-frame/Parseval mechanism already audited in PF-325; continuous tight frames and harmonic group frames are standard frame theory.

A targeted literature check of continuous tight frames and band-limited translation orbits found only this standard abstract background. No external theorem is needed for (5)--(14), and no novelty is claimed for frame theory itself. The project-specific content is the exact combination of PF-323's critical coordinate, PF-325's physical-position Hilbert--Schmidt accounting, PF-326's parity-resolved seam multiplier, and PF-327's compactification-critical shape limit. No new entry in `SOURCES.md` is required.

## Boundaries and falsification

1. **Pre-angle versus completed response.** Equations (10)--(13) are lower scales for the pulled-back packet's compactified transverse energy before physical `L/H` projection, common finite-pant completion, and final intrinsic diagonal normalization. They are not lower bounds for `T_{0,n}^{(r)}` or `B_{n,r}`.
2. **The parity powers can cancel in the intrinsic angle.** The symmetric `w_n^{-1}` and antisymmetric `w_n` scales are real in the seam-pulled raw energy, but the completed diagonal blocks may carry matching factors. No blow-up/vanishing claim is made for the angle itself.
3. **`w_n` and `s_n` are distinct.** PF-328 never substitutes the PF-205 seam half-width for the tight-pant neighboring-cuff scale. The former controls seam normalization; the latter controls the compactification-critical transverse operator.
4. **Fixed physical bandwidth.** `kappa`, `lambda_0`, `lambda_1`, and `R` are fixed before taking the tail. A growing cutoff or a lambda interval approaching zero requires a new uniform analysis.
5. **Positive measure, not global coverage.** The critical interval has fixed nonzero length, not a fixed fraction of the growing cuff. PF-325 nevertheless charges any nonvanishing completed response on such an interval at order one because the frame density `m_n/ell_n` tends a positive constant.
6. **No claim about the conditional channel.** The independent PF-315/PF-316 channel `T_H` remains outside this result.
7. **No RH conclusion.** This finding sharpens one local direct-angle gate. It does not establish compactness, weak trace class, scattering, determinant control, a zeta-zero correspondence, the critical line, or RH.

A refutation would have to break PF-326's uniform fixed-band seam asymptotics, PF-323's exact critical-center identity, PF-327's local energy limit, the elementary Riemann-sum constants in (20)--(21), or PF-325's exact packet-position Hilbert--Schmidt identity. The open question remains whether the downstream one-cusp-pant/physical-projection/completion machinery suppresses the completed response on the positive-length interval identified here.

## Consequence for the research line

The accepted direct-angle clue should now treat the PF-323 critical family as an **interval test**, not a distinguished-center test. Propagate the exact PF-325 seam-normalized packets through the shear-deleted one-cusp pant while keeping the parity scales from (6), and compute the completed response profile on `I_n` in both PF-324 arithmetic boundary regimes.

A positive endpoint proof must make that response vanish in `L^2(I_n)` at the reciprocal-prime PF-318 rate; in particular it must vanish in measure on `I_n`. A negative result need not find a worst single packet: a fixed positive-measure subset of critical centers retaining nonzero completed intrinsic response already kills the Hilbert--Schmidt fallback. The remaining uncertainty is therefore genuinely pant-side and **profile-level**, with both the center measure and the seam normalization now explicit.