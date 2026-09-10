# PC-239 — original-coordinate Bezout winding is ballistic and collapses to shift calculus

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the original-coordinate / `q`-mesh winding escape left explicitly open by PC-238. Fix a coarse conductor `N>1` and let a fresh prime `q -> infinity` run in one invertible residue class modulo `N`. On the refined polygon `mu_{Nq}`, the original coordinate multiplier `Z_q=M_z` is not an additional slowly varying coordinate relative to the two quotient multipliers `U_q=M_{z^q}` and `V_q=M_{z^N}` of PC-238. In the exact CRT coordinates it is

\[
\boxed{
Z_q=R_1\otimes S_q^{-k_q},
\qquad
k_q=\frac{a q-1}{N},
\qquad
ar\equiv1\pmod N,
\quad r=q\bmod N.
}
\]

Thus every fixed original-coordinate Fourier mode whose degree is not divisible by `N` translates the fresh packet by a distance proportional to `q`. On packet-local states those modes converge weakly to zero; the modes divisible by `N` are exactly functions of the already-classified fresh quotient coordinate `z^N`. Consequently, for every fixed `F in C(T)`, the packet-local weak limit of `F(Z_q)` is the finite-group conditional expectation of `F` onto the `mu_N`-invariant subalgebra, followed by the existing bilateral-shift functional calculus.

The norm lost from the packet window is not destroyed: it escapes ballistically to one of finitely many moving windows. But following the source-forced drift does not reveal a new carrier. The exact recentering identity

\[
\boxed{
V_q^{d k_q+h}Z_q^d=U_q^{ad}V_q^h
}
\]

returns every fixed moving channel directly to the commutative CRT quotient algebra of PC-238. If all `N` residue channels are retained simultaneously, `Z_q` converges to the canonical `N`-th-root companion of the bilateral shift; that companion is unitarily equivalent to the ordinary bilateral shift itself. Hence merely retaining the original coordinate `z`, including the information hidden in its growing Bezout exponent, does **not** produce a second local spectral coordinate or a new RH-facing operator carrier.

The exact kinematics below use only `gcd(N,q)=1`, not primality. The same collapse holds with `q` replaced by any coprime integer tending to infinity in the same residue class, providing a matched nonprime control. This finding does not classify deliberately `q`-dependent original-coordinate degrees of order `q`, singular/unbounded functions of `Z_q`, genuinely noncommuting old/new operators applied before coordinate functional calculus, simultaneous `N,q -> infinity`, or global uniformization/accessory data.

## 1. Exact CRT reconstruction of the original refined coordinate

Fix `N>1`. Let `q` be prime with `q \nmid N`, and restrict first to a residue subsequence

\[
r=q\bmod N\in(\mathbb Z/N\mathbb Z)^\times.
\tag{1}
\]

Let `a` be the unique integer with

\[
1\le a<N,
\qquad
ar\equiv1\pmod N,
\tag{2}
\]

and define

\[
\boxed{
k_q=\frac{a q-1}{N}.}
\tag{3}
\]

Because `aq == ar == 1 (mod N)`, `k_q` is an integer. Moreover

\[
\frac{k_q}{q}\longrightarrow\frac aN.
\tag{4}
\]

On `H_{N,q}=ell^2(mu_{Nq})`, let

\[
Z_q=M_z,
\qquad
U_q=M_{z^q}=Z_q^q,
\qquad
V_q=M_{z^N}=Z_q^N.
\tag{5}
\]

PC-238 gives the exact CRT Fourier coordinates

\[
H_{N,q}\cong\mathbb C^N\otimes\ell^2(\mathbb Z/q\mathbb Z),
\qquad
U_q=R_r\otimes I,
\qquad
V_q=I\otimes S_q,
\tag{6}
\]

where `R_r` is translation by `r` on `Z/NZ` and `S_q` is translation by one on `Z/qZ`.

The definition (3) gives

\[
Nk_q+1=aq.
\tag{7}
\]

Therefore, directly at finite `q`,

\[
V_q^{k_q}Z_q
=Z_q^{Nk_q+1}
=Z_q^{aq}
=U_q^a.
\tag{8}
\]

Since `R_r^a=R_1`, (6)--(8) yield the exact formula

\[
\boxed{
Z_q=R_1\otimes S_q^{-k_q}.
}
\tag{9}
\]

Equivalently, if `Nbar_q` is the inverse of `N modulo q`, then

\[
\overline N_q\equiv-k_q\pmod q.
\tag{10}
\]

Equation (9) is the precise form of the growing-Bezout-exponent phenomenon that PC-238 deliberately left outside its equicontinuous joint calculus. It is not an arbitrary fast profile: it is the unique winding forced by reconstruction of the original coordinate from the two source quotient coordinates.

## 2. Fixed original-coordinate degrees have a sharp ballistic dichotomy

Take any fixed integer `c`. Write it uniquely as

\[
c=N\ell+d,
\qquad
0\le d<N.
\tag{11}
\]

Raising (9) to the `c`-th power and using (7), one gets

\[
\boxed{
Z_q^c
=R_d\otimes S_q^{\,\ell-dk_q}.
}
\tag{12}
\]

Indeed `-c k_q == ell-d k_q (mod q)` because `Nk_q == -1 (mod q)`.

There are now exactly two cases. If `d=0`, then

\[
Z_q^{N\ell}=I\otimes S_q^\ell=V_q^\ell,
\tag{13}
\]

so the mode is already in the fresh quotient calculus. If `d != 0`, then from (4)

\[
\frac{\ell-dk_q}{q}\longrightarrow-\frac{da}{N}
\quad\text{in }\mathbb R/\mathbb Z.
\tag{14}
\]

Because `a` is a unit modulo `N` and `1<=d<N`, `da` is nonzero modulo `N`. Hence the cyclic distance of the shift exponent from zero satisfies

\[
\boxed{
\lim_{q\to\infty}
\frac1q\operatorname{dist}_{\mathbb Z/q\mathbb Z}
(\ell-dk_q,0)
=
\left\|\frac{da}{N}\right\|_{\mathbb R/\mathbb Z}
\ge\frac1N.
}
\tag{15}
\]

Thus every fixed degree not divisible by `N` is a **ballistic fresh translation**. The escape speed is source-forced and separated uniformly from zero on a fixed coarse conductor.

This already rules out the most naive interpretation of the original coordinate as an additional packet-local variable. The original coordinate does contain the CRT Bezout information suppressed by equicontinuity in PC-238, but that information appears as macroscopic transport rather than as a second slowly varying local coordinate.

## 3. Packet-local weak limit is finite-group conditional expectation

The packet limits of PC-227 and PC-235 identify bounded windows in the fresh cyclic index with bounded windows in `ell^2(Z)`. The only property needed here is the resulting tightness. Let `xi_q, eta_q` be vector families that, after the source packet identifications, converge in norm to `xi, eta` in a fixed finite direct sum of copies of `ell^2(Z)`.

If `h_q in Z/qZ` satisfies

\[
\operatorname{dist}_{\mathbb Z/q\mathbb Z}(h_q,0)\longrightarrow\infty,
\tag{16}
\]

then

\[
\boxed{
\langle\eta_q,S_q^{h_q}\xi_q\rangle\longrightarrow0.
}
\tag{17}
\]

This is elementary: approximate `xi` and `eta` in norm by finite-support vectors. For large `q`, (16) makes the shifted support disjoint from the other finite support; the remaining terms are bounded by the two norm tails. It is the packet form of the standard fact that high powers of the bilateral regular shift converge weakly to zero, equivalently the Riemann--Lebesgue decay of its matrix coefficients in the `L^2(T)` model.

Combining (12), (15), and (17), for each fixed integer `c=N ell+d`,

\[
\boxed{
\lim_{q\to\infty}
\langle\eta_q,Z_q^c\xi_q\rangle
=
\begin{cases}
\langle\eta,(I\otimes S^\ell)\xi\rangle,&d=0,\\[2mm]
0,&d\ne0.
\end{cases}
}
\tag{18}
\]

The result extends from Laurent monomials to every fixed continuous function `F in C(T)`. Define the canonical finite-group average

\[
(\mathcal E_NF)(z)
=
\frac1N\sum_{\omega^N=1}F(\omega z).
\tag{19}
\]

This removes precisely the Fourier degrees not divisible by `N`. The averaged function is invariant under multiplication by `mu_N`, so there is a unique `G_F in C(T)` satisfying

\[
(\mathcal E_NF)(z)=G_F(z^N).
\tag{20}
\]

Uniform Laurent approximation on `T`, together with `||F(Z_q)||<=||F||_infty`, upgrades (18) to

\[
\boxed{
\lim_{q\to\infty}
\langle\eta_q,F(Z_q)\xi_q\rangle
=
\langle\eta,(I\otimes G_F(S))\xi\rangle.
}
\tag{21}
\]

Thus the packet-local limit of a fixed continuous original-coordinate observable is exactly the conditional expectation onto the `mu_N`-invariant subalgebra, followed by the already-known fresh bilateral-shift calculus. The rapidly winding Bezout reconstruction does not survive locally as a new coordinate.

The topology matters. Equation (21) is a **weak, packet-local statement**, not strong operator convergence. For example `F(z)=z` has local weak limit zero when `N>1`, while

\[
\|Z_q\xi_q\|=\|\xi_q\|.
\tag{22}
\]

The missing norm has escaped to a remote packet window. Treating (21) as annihilation would therefore be wrong; the next section tracks the escaped mass exactly.

## 4. Following the ballistic channel returns exactly to the PC-238 algebra

For every fixed residue degree `d` and every fixed integer offset `h`, equations (7)--(9) give the finite-level identity

\[
\boxed{
V_q^{d k_q+h}Z_q^d
=U_q^{ad}V_q^h.
}
\tag{23}
\]

The left side follows the `d`-th original-coordinate ballistic channel by the canonical countershift `d k_q`, with an optional bounded offset. The right side lies **exactly**, not just asymptotically, in the commutative joint quotient algebra generated by `U_q` and `V_q`.

Consequently, recentering around the escaped packet does not uncover a hidden noncommuting degree of freedom. Every fixed moving frame within `O(1)` of the source-forced drift reduces to one finite coarse translation and one bounded fresh translation. A moving frame whose velocity differs by a nonzero amount remains ballistically separated and is packet-weakly zero by (17).

The same observation controls fixed finite words with regular PC-238 coefficients. A bounded number of insertions of powers `Z_q^d`, interspersed with fixed Laurent polynomials in `U_q,V_q`, has a total residue degree modulo `N`. If that degree is nonzero, its fresh translation is still ballistic; if it is zero, the total word reduces to the joint quotient algebra. Uniform approximation extends the statement to fixed continuous coefficients on the CRT cylinder whenever no `q`-dependent mesh scale is inserted by hand.

## 5. Retaining every escaped residue channel still gives one bilateral shift

One could object that a packet-local window is too small: perhaps the arithmetic content lives in the entire finite collection of windows reached by the original coordinate. Keep all `N` residue channels

\[
\mathcal W_{d,q}=Z_q^d\mathcal W_{0,q},
\qquad
0\le d<N.
\tag{24}
\]

For distinct `d,e`, the fresh centers differ by `(d-e)k_q`. By (15), their normalized cyclic separation is bounded away from zero, so the channels become mutually orthogonal at packet scale.

After identifying each moving window with one copy of `ell^2(Z)`, the original coordinate acts in the limit by

\[
\boxed{
T_N(e_d\otimes f)=
\begin{cases}
e_{d+1}\otimes f,&0\le d<N-1,\\
e_0\otimes Sf,&d=N-1.
\end{cases}
}
\tag{25}
\]

In particular

\[
T_N^N=I\otimes S.
\tag{26}
\]

This companion/root operator may look like a larger carrier, but it is merely the ordinary bilateral shift with a finer indexing. Define

\[
J(e_d\otimes e_j)=e_{Nj+d}
\quad
(0\le d<N,\ j\in\mathbb Z).
\tag{27}
\]

Then `J` is unitary from `C^N tensor ell^2(Z)` to `ell^2(Z)` and

\[
\boxed{
JT_NJ^*=S.
}
\tag{28}
\]

Hence

\[
C^*(T_N)\cong C^*(S)\cong C(\mathbb T).
\tag{29}
\]

Keeping all ballistic channels restores the norm missing from (21), but it does **not** create an enlarged spectral algebra. It reconstructs the universal one-dimensional regular translation.

## 6. Geometric control: the anchored original chord becomes universal

The most direct geometry depending on the original coordinate is the common-anchor chord

\[
|1-z|^2=2-z-z^{-1}.
\tag{30}
\]

For `N>1`, the degrees `+1` and `-1` are not divisible by `N`. Equation (21) therefore gives the packet-local weak limit

\[
\boxed{
2I.
}
\tag{31}
\]

If all `N` moving channels are retained instead, (25) gives

\[
\boxed{
2I-T_N-T_N^*.
}
\tag{32}
\]

By (28), this is unitarily equivalent to the standard bilateral discrete-Laplacian symbol `2-S-S^*`, with spectrum `[0,4]`. Thus even the source-native chord from the common anchored vertex to the refined point acquires no new spectral set from the growing Bezout winding: locally its off-diagonal pieces escape; globally across the finite channel completion it is the universal lattice chord operator.

## 7. Matched nonprime control

Primality was not used in (3), (7)--(15), (23), or the channel completion. Replace `q` by any integer `m` with

\[
\gcd(m,N)=1,
\qquad
m\equiv r\pmod N,
\qquad
m\to\infty.
\tag{33}
\]

With

\[
k_m=\frac{am-1}{N},
\tag{34}
\]

the same exact CRT reconstruction, ballistic velocities, recentering identities, conditional-expectation limit, and `N`-channel bilateral-shift completion hold verbatim.

This is a control on the **coordinate/operator carrier**, not a claim that every source state at conductor `Nm` equals the fresh-prime source packet of PC-227. Arithmetic can remain in a source amplitude or old/new state. What this control rules out is attributing primality or RH-facing content to the original-coordinate Bezout kinematics themselves: those kinematics are identical for matched coprime composite refinements.

## 8. Prior art and novelty audit

All abstract ingredients are classical. The CRT tensorization in Section 1 is the same finite abelian product structure used by prime-factor/Good--Thomas Fourier decompositions. The finite average (19) is the canonical expectation from `C(T)` onto the fixed-point algebra for the action of the finite group `mu_N`; finite-group averaging as a conditional expectation is standard in operator-algebra theory. The weak disappearance of translations in (17) is the regular-representation/Riemann--Lebesgue mechanism for the bilateral shift, and (28) is an explicit unitary reindexing rather than a new shift theorem.

A directed literature check against cyclic/CRT Fourier theory, finite-group fixed-point expectations, bilateral-shift weak limits, and Bost--Connes/cyclotomic dynamics found no basis for a historical novelty claim or for interpreting this mechanism as an independent zeta operator. The Bost--Connes system, in particular, obtains arithmetic dynamics from a substantially richer semigroup/crossed-product structure; the carrier isolated here is only the ordinary regular shift after exact source-forced recentering. Standard literature anchors include the classical prime-factor FFT/CRT decomposition, the canonical fixed-point expectation for finite group actions (for example the finite-group C*-algebra literature around Watatani index and Jeong--Park), and the usual `L^2(T)` model of the bilateral shift.

No historical novelty is claimed for CRT, Bezout inversion, group averaging, Riemann--Lebesgue decay, companion shifts, or bilateral-shift functional calculus. The project-specific durable result is narrower and exact: **the particular non-equicontinuous winding forced by reconstructing the original Prime-Circle coordinate, which was outside PC-238, is ballistic; its local weak limit is conditional expectation, and its complete finite moving-frame resolution is again the universal bilateral shift.**

Nothing in the derivation produces a zeta factor, gamma factor, functional equation, explicit-formula zero term, or a distinguished real part `1/2`. Adding any of those through a chosen `q`-dependent function would require a separate source-forced mechanism.

## 9. Exact boundary and consequence for the Prime-Circle frontier

This finding closes the fixed-base route

\[
\boxed{
\text{PC-238 growing Bezout reconstruction of }z
\longrightarrow
\text{fixed continuous original-coordinate observable}
\longrightarrow
\text{packet-local or finitely recentered spectral carrier}
\longrightarrow
\text{new RH mechanism}.
}
\tag{35}
\]

It also closes fixed finite Laurent words formed from regular joint quotient coefficients and a bounded number of original-coordinate insertions: nonzero total degree modulo `N` escapes ballistically, while degree zero returns to the PC-238 algebra. Tracking all `N` source-forced escape channels merely reconstructs the ordinary bilateral shift.

The theorem deliberately does **not** classify:

- original-coordinate degrees or profiles that themselves vary with `q` on an `O(q)` scale and couple several ballistic velocities at once;
- singular or unbounded functions of `Z_q` for which continuous functional calculus and uniform approximation do not apply;
- genuinely noncommuting old/new, transfer, or two-dimensional operators acting before scalar coordinate functional calculus;
- simultaneous coarse/fresh growth `N,q -> infinity`;
- global uniformization, monodromy, or accessory data.

Those are real boundaries, not invitations to arbitrary spectral engineering. Any surviving `q`-mesh construction must derive its growing degree, singularity, velocity coupling, or noncommutativity from the Prime-Circle source itself and must survive matched coprime-composite controls. **Merely retaining the original refined coordinate `z` is no longer enough.**