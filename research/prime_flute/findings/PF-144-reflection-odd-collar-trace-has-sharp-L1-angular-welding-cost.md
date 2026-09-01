# PF-144 — reflection-odd collar trace has sharp `L^1` angular welding cost

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-143 proves that a genuinely nonconstant angular trace on the thick-scale boundary of a pinching standard collar cannot be made cheap merely because the core length tends to zero: every tail-near-isometric angular welding pays at least a constant times the centered `L^1` trace amplitude. The present finding proves the matching upper bound for the canonically relevant reflection-odd sector. A simple nonlinear soft-threshold extension realizes any sufficiently small `C^1` reflection-odd boundary displacement with Güneysu--Thalmaier inverse-unit-ball weighted cost `O(||psi||_1)`, uniformly in the collapsing core length, while its bilipschitz constant tends to `1` whenever the boundary trace is `C^1`-small. Thus the angular part of the remaining wave-operator interface problem has an exact local currency: **unweighted `L^1` trace amplitude**, neither a collapse-suppressed quantity nor a stronger `W^{1,1}` derivative budget. This does not prove that the actual prime/shift-clone trace amplitudes are summable and does not treat the transverse/radial collar-body shape mismatch.

## Claim

Let

\[
C_L^+=[0,w(L)]\times\mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

be a standard hyperbolic half-collar with

\[
g_L=dr^2+s_L(r)^2d\theta^2,
\qquad
s_L(r)=L\cosh r,
\qquad
\theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Normalize the angular origin by the PF-142 marked reflection points. Let

\[
\psi\in C^1(\mathbb S^1)
\tag{3}
\]

be a periodic lift satisfying

\[
\boxed{
\psi(-\theta)=-\psi(\theta),
\qquad
\psi(0)=\psi(1/2)=0.
}
\tag{4}
\]

Put

\[
A:=\|\psi\|_{L^\infty},
\qquad
E:=\|\psi'\|_{L^\infty},
\qquad
\varepsilon:=\max\{A,E\}.
\tag{5}
\]

There are absolute constants `L_0>0`, `epsilon_0>0`, and `C>0` such that, whenever

\[
0<L<L_0,
\qquad
\varepsilon<\varepsilon_0,
\tag{6}
\]

there is a reflection-equivariant degree-one bi-Lipschitz angular self-map

\[
F_\psi:C_L^+\longrightarrow C_L^+,
\qquad
F_\psi(r,\theta)=(r,\theta+u(r,\theta)),
\tag{7}
\]

with outer-boundary trace

\[
F_\psi(w(L),\theta)
=(w(L),\theta+\psi(\theta)),
\tag{8}
\]

which is the identity outside the outer unit collar slab and satisfies

\[
\boxed{
\operatorname{Bilip}(F_\psi)
\le1+C\varepsilon.
}
\tag{9}
\]

If

\[
\mathcal W_L(F_\psi)
:=
\int_{C_L^+}
\mu_{g_L}(B_{g_L}(z,1))^{-1}
\delta_{g_L,F_\psi^*g_L}(z)
\,d\mu_{g_L}(z)
\tag{10}
\]

is the same local Güneysu--Thalmaier weighted metric-deviation functional used in PF-128/PF-143, then

\[
\boxed{
\mathcal W_L(F_\psi)
\le C\|\psi\|_{L^1(\mathbb S^1)}
}
\tag{11}
\]

with `C` independent of `L` and of the frequency content of `psi`.

Combining (11) with PF-143, whose lower bound applies to every tail-near-isometric angular welding and whose centering is automatic under (4), gives the sharp two-sided local scale

\[
\boxed{
 c\|\psi\|_{L^1}
\le
\inf_{F\in\mathcal A(\psi)}\mathcal W_L(F)
\le
C\|\psi\|_{L^1},
}
\tag{12}
\]

where `A(psi)` denotes the angular collar maps in the PF-143 near-isometric regime with marked outer trace `theta -> theta+psi(theta)`. The constants in (12) are uniform as `L->0`.

Therefore, for a family of actual PF-142-normalized collar traces `psi_eta` satisfying

\[
\|\psi_\eta\|_\infty
+
\|\psi_\eta'\|_\infty
\longrightarrow0,
\tag{13}
\]

the **angular** part of the wave-weight assembly is summable whenever

\[
\boxed{
\sum_\eta\|\psi_\eta\|_{L^1}<\infty.
}
\tag{14}
\]

Conversely, PF-143 shows that (14) is necessary for finite total cost inside this angular near-isometric welding class. PF-144 does not establish (13) or (14) for the actual prime/shift-clone body traces; it identifies the correct local norm once those traces are known.

## 1. The outer unit slab is uniformly thick even when the collar core collapses

Introduce inward distance from the outer standard-collar boundary,

\[
y:=w(L)-r,
\qquad 0\le y\le1.
\tag{15}
\]

The angular circumference scale on this slab is

\[
\begin{aligned}
a_L(y)
&:=s_L(w(L)-y)\\
&=L\cosh(w(L)-y)\\
&=L\coth(L/2)\cosh y
-L\operatorname{csch}(L/2)\sinh y.
\end{aligned}
\tag{16}
\]

Hence, uniformly for `0<=y<=1`,

\[
\boxed{
a_L(y)\longrightarrow2e^{-y}}
\qquad(L\to0),
\tag{17}
\]

and therefore there are absolute constants `0<c_0<C_0<infinity` such that

\[
\boxed{
c_0\le a_L(y)\le C_0}
\tag{18}
\]

through the entire outer unit slab for every sufficiently small `L`.

PF-128 gives the ambient unit-ball lower estimate

\[
\mu_{g_L}(B_{g_L}(z,1))
\ge c\min\{1,s_L(r)\}.
\tag{19}
\]

Equations (18)--(19) imply on this slab

\[
\boxed{
\mu_{g_L}(B_{g_L}(z,1))\asymp1,
\qquad
d\mu_{g_L}=a_L(y)\,dy\,d\theta\asymp dy\,d\theta.
}
\tag{20}
\]

Thus the Güneysu--Thalmaier weighted measure is uniformly comparable to flat product measure there. This is exactly the region in which PF-143 obtained its lower trace bound; no shrinking factor from the core length survives at the interface.

## 2. A nonlinear soft-threshold extension spends only the `L^1` trace mass

For `t>=0` define the scalar soft-threshold map

\[
S_t(q):=\operatorname{sgn}(q)(|q|-t)_+.
\tag{21}
\]

If `psi` is not identically zero, define on the outer slab

\[
\boxed{
u(y,\theta):=S_{\varepsilon y}(\psi(\theta)),}
\tag{22}
\]

and put `u=0` deeper in the collar. If `psi=0`, take the identity map.

Because `epsilon>=A`, equation (22) already vanishes for every `y>=A/epsilon<=1`. Thus the extension is supported inside the outer unit slab and has the exact boundary trace

\[
u(0,\theta)=\psi(\theta).
\tag{23}
\]

The map is Lipschitz and piecewise `C^1`; away from its measure-zero free boundary `|psi(theta)|=epsilon y`, its derivatives are

\[
\boxed{
|u_y|
=\varepsilon\,
\mathbf 1_{\{|\psi|>\varepsilon y\}},
\qquad
u_\theta
=\psi'(\theta)
\mathbf 1_{\{|\psi|>\varepsilon y\}}.
}
\tag{24}
\]

In particular,

\[
\|u_y\|_\infty\le\varepsilon,
\qquad
\|u_\theta\|_\infty\le E\le\varepsilon.
\tag{25}
\]

The two integrated derivative costs are sharper. By Fubini,

\[
\begin{aligned}
\int_0^1\int_{\mathbb S^1}|u_y|\,d\theta dy
&=
\int_{\mathbb S^1}
\varepsilon\frac{|\psi(\theta)|}{\varepsilon}
\,d\theta\\
&=\boxed{\|\psi\|_{L^1},}
\end{aligned}
\tag{26}
\]

while

\[
\begin{aligned}
\int_0^1\int_{\mathbb S^1}|u_\theta|\,d\theta dy
&=
\frac1\varepsilon
\int_{\mathbb S^1}
|\psi'(\theta)|\,|\psi(\theta)|\,d\theta\\
&\le
\frac E\varepsilon\|\psi\|_{L^1}\\
&\le\boxed{\|\psi\|_{L^1}.}
\end{aligned}
\tag{27}
\]

This is the useful endpoint cancellation. A high-frequency trace is not charged by its full `L^1` derivative because the extension depth at angle `theta` is only

\[
\frac{|\psi(\theta)|}{\varepsilon}.
\tag{28}
\]

The nonlinear support automatically becomes thinner where the boundary amplitude is smaller.

## 3. The soft-threshold map stays near-isometric

In the orthonormal source/target frames used in PF-143, the differential of the angular map has the form

\[
M=
\begin{pmatrix}
1&0\\
a&q
\end{pmatrix},
\qquad
a=a_L(y)u_y,
\qquad q=1+u_\theta.
\tag{29}
\]

Equations (18) and (25) give

\[
|a|+|q-1|\le C\varepsilon.
\tag{30}
\]

For sufficiently small `epsilon`, `q>0`, so every circle map has degree one and is orientation preserving. Moreover

\[
\|M^TM-I\|\le C\varepsilon,
\tag{31}
\]

which proves (9). The same finite-dimensional estimate gives the complementary local upper bound to PF-143's equation (18):

\[
\boxed{
\delta_{g_L,F_\psi^*g_L}
\le C\bigl(a_L|u_y|+|u_\theta|\bigr)
}
\tag{32}
\]

in the present small-distortion regime.

Using (20), (32), and the boundedness of `a_L`,

\[
\begin{aligned}
\mathcal W_L(F_\psi)
&\le
C\int_0^1\int_{\mathbb S^1}
\left(|u_y|+|u_\theta|\right)d\theta dy\\
&\le C\|\psi\|_{L^1}
\end{aligned}
\tag{33}
\]

by (26)--(27). This proves (11).

The hard threshold in (21) is only a convenient exact formula. The resulting map is bi-Lipschitz and piecewise smooth, which is enough for the local metric-cost statement. If a later global scattering proof requires a smooth diffeomorphism, the free-boundary corners must be rounded while preserving the same summable budget; PF-144 deliberately does not invoke Güneysu--Thalmaier at that later global step.

## 4. Reflection symmetry and marked anchors are preserved automatically

Soft thresholding is odd in its scalar argument:

\[
S_t(-q)=-S_t(q).
\tag{34}
\]

Therefore (4) implies

\[
u(y,-\theta)=-u(y,\theta),
\tag{35}
\]

so

\[
F_\psi\circ\rho=\rho\circ F_\psi
\tag{36}
\]

for the standard collar reflection `rho(r,theta)=(r,-theta)`. Because `psi(0)=psi(1/2)=0`, both PF-142 marked fixed rays remain fixed throughout the correction. No constant rotation phase is introduced.

This matters globally. PF-142 removed the constant mode by choosing the canonical reflection-equivariant marking. PF-144 stays inside exactly that gauge rather than solving the angular extension problem by reintroducing an arbitrary phase.

## 5. PF-143's lower bound is sharp in the norm that matters

PF-143 proves for every angular near-isometry with outer displacement `psi`

\[
\mathcal W_L(F)
\ge c\|\psi^\circ\|_{L^1},
\tag{37}
\]

uniformly in the collapsing core length. Under the reflection normalization (4), `psi` is odd and hence centered, so

\[
\psi^\circ=\psi.
\tag{38}
\]

The upper construction (33) therefore matches the lower estimate in the same norm. In particular,

\[
\boxed{
\text{nonconstant angular interface cost}
\asymp
\|\psi\|_{L^1}
}
\tag{39}
\]

within the marked tail-near-isometric angular welding class, with constants independent of `L`.

This has two consequences for how the accepted wave clue should be attacked.

First, **pinching neither helps nor hurts this mode**. There is no hidden factor `L`, `1/L`, `log(1/L)`, or collar width in the optimal local scale. PF-141's `O(L|tau|)` gain belongs only to the constant phase sector, which PF-142 already removes canonically.

Second, a stronger trace norm is not forced. In particular, the fact that `psi'` might have a much larger or even globally nonsummable `L^1` ledger does not by itself obstruct angular welding. The adaptive depth (28) makes the integrated tangential cost proportional to the amplitude mass instead.

## 6. Consequence for the shift-clone wave-operator clue

After PF-138--PF-143, the closed-thin interface problem had two surviving pieces:

\[
\text{reflection-odd angular trace}
+\text{transverse/radial shape mismatch}.
\tag{40}
\]

PF-144 resolves the **local functional form** of the first piece. Suppose the actual globally marked body map induces on the `eta`th normalized short-collar boundary a reflection-odd angular mismatch `psi_eta` with `C^1` size tending to zero. Then the angular corrections can be inserted with tail bilipschitz constants tending to one and finite total Güneysu--Thalmaier weight whenever (14) holds.

By PF-143, if

\[
\sum_\eta\|\psi_\eta\|_1=\infty,
\tag{41}
\]

then no collection of angular-only tail-near-isometric weldings can have finite total weight. A future negative argument would still have to show that the **actual** trace sequence really has this divergence, or prove that every more general transverse/radial comparison pays an equivalent unavoidable cost. PF-144 does neither.

Thus the angular gate is no longer the vague requirement for a `W^{1,1}`-type trace estimate. It is the concrete question

\[
\boxed{
\text{are the actual PF-142-normalized amplitudes }
\|\psi_\eta\|_{L^1}
\text{ summable?}
}
\tag{42}
\]

followed independently by the transverse/radial collar-body compatibility problem.

## 7. Stress tests and scope boundaries

1. **Constant phase.** A constant `psi=tau` is not in the reflection-odd marked sector unless `tau=0`. The construction would give an `O(|tau|)` upper bound, but PF-141's `O(L|tau|)` central shear is much better. There is no contradiction because PF-143 centers away the constant mode and PF-142 eliminates it canonically.
2. **High frequency.** High frequency does not create a separate integrated derivative tax as long as the actual circle map remains `C^1`-small. Equation (27) is frequency-independent after the factor `E/epsilon<=1`. If `E` is not small, the map need not be tail-near-isometric and the claim does not apply.
3. **Collapse.** The construction uses only the outer unit slab, where (18) gives uniformly thick geometry. It neither exploits nor suffers the shrinking core circumference. This is why the constants are independent of `L`.
4. **Trace regularity.** The explicit formula is stated for `C^1` traces because the wave-comparison program needs near-isometric marked homeomorphisms. General `L^1` trace extension is a different, classical endpoint Sobolev question and is not needed here.
5. **Transverse/radial mismatch.** PF-144 preserves the radial coordinate and assumes the two standard collar boundaries have already been identified. It says nothing about straightening a body image that arrives on a nonstandard transverse curve. That remains an independent gate.
6. **Actual arithmetic sequence.** No estimate for `sum ||psi_eta||_1` is derived from prime gaps here. The finding calibrates the geometric cost once the actual traces are computed.
7. **Wave operators.** Even (14) would settle only the angular component of the collar insertion. One complete smooth globally marked comparison with finite total weighted deviation is still required before applying Güneysu--Thalmaier.
8. **Spectral/RH interpretation.** The result is a local hyperbolic interface lemma. It creates no prime-specific selector and has no direct RH implication.

## 8. Prior-art / novelty audit

The endpoint philosophy behind (11) is classical rather than a new trace theorem. Gagliardo's trace theorem characterizes traces of Sobolev functions on Lipschitz boundaries; in the endpoint `W^{1,1}` case the trace map onto `L^1` is surjective and bounded nonlinear extension constructions are classical. See E. Gagliardo, *Caratterizzazioni delle tracce sulla frontiera relative ad alcune classi di funzioni in n variabili*, Rend. Sem. Mat. Univ. Padova 27 (1957), 284--305. Modern discussions of the endpoint also emphasize that the useful right inverse is necessarily nonlinear in general.

Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supplies the weighted scattering criterion that motivates `W_L`; it does not provide this boundary welding construction. Standard collar geometry, trace inequalities, and nonlinear Sobolev extension ideas likewise do not by themselves identify the exact local cost of the PF-142 reflection-odd interface.

Directed searches for `W^{1,1}`/`L^1` trace extension, nonlinear endpoint extensions, hyperbolic collar angular interpolation, and metric-scattering perturbations located the classical trace theory and the existing Güneysu--Thalmaier criterion, but no theorem directly combining: (i) a collapsing hyperbolic standard collar, (ii) marked reflection-equivariant degree-one angular maps, (iii) tail bilipschitz constant tending to one, and (iv) a two-sided `L^1` characterization of the inverse-unit-ball weighted metric-deviation cost.

No broad novelty is claimed. The durable project-specific contribution is the explicit soft-threshold map (22) and the exact cancellation (26)--(27), combined with PF-143's lower bound to sharpen the accepted prime/shift-clone wave-assembly gate from an unspecified trace-regularity problem to the concrete `L^1` amplitude condition (14).

## 9. Falsification core

A later adversary can test PF-144 through a short independent chain:

1. derive (16) from the standard collar width and verify the uniform outer-slab bounds (18);
2. combine PF-128's unit-ball lower estimate with (18) to obtain the weighted-measure upper comparison (20);
3. differentiate the soft threshold (22) almost everywhere and verify (24)--(27), especially that the active radial depth is exactly `|psi(theta)|/epsilon`;
4. write the orthonormal differential matrix (29), check `q>0`, and derive both the bilipschitz estimate (9) and the pointwise upper deviation bound (32);
5. integrate (32) using (20), (26), and (27) to obtain (11);
6. verify that oddness and the two PF-142 anchors are preserved exactly;
7. import only PF-143's already-proved lower bound and center it using oddness to obtain (12);
8. confirm that no step estimates the actual prime/shift trace sequence or the transverse/radial interface.

A failure in steps 1--5 refutes the local upper bound. Failure of actual trace summability would not refute PF-144; it would give the precise angular obstruction that PF-144 and PF-143 together isolate.