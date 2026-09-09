# PC-235 — fresh-scale packet tangent is universal Laurent-shift calculus

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY` for two explicit fixed-base escapes left open by PC-233/PC-234: a geometry-forced non-rotation-invariant operator that mixes the fresh Fourier modes, and a renormalized `1/q`-scale correction to a smooth regular-polygon multiplier. On the full `Nq`-gon the canonical fresh-fiber coordinate `z^N` is multiplication in the vertex basis and therefore shifts target Fourier labels by `N`. In the exact PC-227 packet coordinate this is **exactly the bilateral unit shift** `j -> j+1`. The common-anchor fresh-fiber chord observable `|1-z^N|^2` is consequently the discrete Laplacian `2I-S-S^{-1}` and sends every shifted Cauchy packet to a finite rational combination of the same integer-translated poles.

The complementary fresh-scale magnification is equally rigid. If a smooth macroscopic Fourier multiplier has symbol `m(k/(Nq))`, then PC-231's exact packet label gives the formal first tangent `-m'(x)J_sigma`, where `J_sigma f(j)=(j+sigma)f(j)` and `x` is the coarse packet center. But a nonzero PC-227 Cauchy packet `C/(j+sigma)` is **not in the domain of `J_sigma`**: `J_sigma f` is the non-square-summable constant sequence. Hence the naive `q`-renormalized subleading multiplier does not define a new bounded packet operator; its norm on the source-forced packet diverges whenever `m'(x) != 0`. The same domain obstruction occurs at the first nonzero higher Taylor order.

Renormalized commutators do remain bounded, but they classicalize completely. For the exact fresh-fiber shift `S_h`,

\[
q[D_m,S_h]\longrightarrow h\,m'(x)S_h
\]

on every limiting packet, and finite nested commutators give only products of the same scalar derivatives times `S_h`. Together with `J_sigma`, these operators generate the standard polynomial-coefficient Laurent-shift algebra

\[
S J_\sigma=(J_\sigma+1)S,
\]

whose commutation geometry is independent of the cyclotomic fractional shift because `J_sigma=J_0+sigma I`. Thus the first source-forced mode mixer, the first fresh-scale tangent, and their canonical noncommutativity do not provide a new cross-prime spectral state at fixed base. They reduce to classical difference-operator/Heisenberg shift calculus acting on the already-known Cauchy packets.

This does **not** classify non-Laurent mode mixing forced by the full old/new geometry, shift support or operator degree growing with `q`, singular/non-smooth multipliers, simultaneous `N,q -> infinity`, operators coupling several packet sectors or several new prime directions before the fixed-base limit, or global uniformization/accessory data.

## 1. The power-map fiber supplies an exact mode shift

Keep the fixed-base setup of PC-227. Let `N>1`, let `q` be a prime with `q \nmid N`, put

\[
M=Nq,
\]

and consider a nonzero packet sector of the normalized cyclotomic transfer `T_{N,q}`. PC-231 gives the exact target Fourier label

\[
\boxed{
k_{t,j}^{(q)}
\equiv q(u-t)-Nj-s\pmod{Nq},
}
\tag{1}
\]

where `s in {1,...,N-1}`, `sigma=s/N`, and the corresponding limiting packet is

\[
\boxed{
f_\sigma(j)=\frac{C}{j+\sigma},
\qquad C\ne0.
}
\tag{2}
\]

The map `z -> z^N` is not an added coordinate choice: on `mu_{Nq}` it is the canonical quotient to the fresh `q`-th-root fiber and preserves the common anchor `1`. Let `Z_N` denote multiplication in the vertex basis by this coordinate,

\[
(Z_NF)(z)=z^N F(z).
\tag{3}
\]

In the Fourier basis of the full regular `M`-gon,

\[
Z_N e_k=e_{k+N}.
\tag{4}
\]

Therefore the coefficient of `Z_NT_{N,q}e_u` at the packet label `k_{t,j}^{(q)}` is the original transfer coefficient at

\[
k_{t,j}^{(q)}-N=k_{t,j+1}^{(q)}.
\tag{5}
\]

Thus, under the same canonical packet identification used in PC-227,

\[
\boxed{Z_N\longrightarrow S,
\qquad (Sf)(j)=f(j+1).}
\tag{6}
\]

More generally `Z_N^h -> S_h`, `(S_hf)(j)=f(j+h)`, for every fixed integer `h`. This is exact at the level of packet labels; no asymptotic phase or gauge is being chosen.

Consequently every fixed Laurent polynomial in the source-forced fresh-fiber coordinate,

\[
V(z^N)=\sum_{h=-H}^{H}v_h z^{Nh},
\tag{7}
\]

acts in the packet limit as the finite Laurent operator

\[
\boxed{V(S)=\sum_{h=-H}^{H}v_hS_h.}
\tag{8}
\]

It mixes the fine target Fourier modes and is therefore genuinely outside the diagonal-multiplier hypothesis of PC-233, but it introduces no new packet coordinate.

## 2. The anchored fresh-fiber chord stays inside the Cauchy packet algebra

The most direct real geometric observable built from (3) and the common anchor is the squared chord in the fresh quotient,

\[
|1-z^N|^2=2-z^N-z^{-N}.
\tag{9}
\]

Its packet-limit operator is therefore

\[
\boxed{L_{\rm fib}=2I-S-S^{-1}.}
\tag{10}
\]

Writing `x=j+sigma`, equation (2) gives the exact rational identity

\[
\begin{aligned}
L_{\rm fib}f_\sigma(j)
&=C\left(\frac2x-\frac1{x+1}-\frac1{x-1}\right)\\
&=\boxed{-\frac{2C}{x(x^2-1)}}.
\end{aligned}
\tag{11}
\]

Thus even the simplest geometry-forced non-rotation-invariant mode mixer does not leave the packet algebra. It only replaces one simple shifted Cauchy pole by a finite partial-fraction combination at the integer translates `sigma-1,sigma,sigma+1`. Since integer translation does not change the fractional shift in `R/Z`, the cyclotomic packet center remains the same.

The same conclusion holds for every fixed Laurent polynomial (7): it produces only finitely many integer translates of the packet. Combining this with PC-231/PC-232 shows that finite pointwise products, convolutions, and fixed fresh-fiber Laurent shifts still remain in the rational-shift/confluent Cauchy algebra. The new operator is non-diagonal in Fourier space, but its mode mixing is the regular representation of the already present cyclic fiber.

## 3. The fresh-scale Taylor tangent is a lattice position operator

PC-231's exact packet label also gives the normalized target frequency

\[
\boxed{
\frac{k_{t,j}^{(q)}}{Nq}
\equiv
x-\frac{j+\sigma}{q}
\pmod1,
\qquad
x:=\frac{u-t}{N}\pmod1.
}
\tag{12}
\]

Let `D_m` be the bounded full-polygon Fourier multiplier of PC-233, with a `C^d` symbol `m` on the circle. Define on finitely supported packet sequences

\[
(J_\sigma f)(j)=(j+\sigma)f(j).
\tag{13}
\]

Taylor expansion of `m` at the coarse center gives, for every fixed packet coordinate `j`,

\[
m\!\left(x-\frac{j+\sigma}{q}\right)
=
\sum_{\ell=0}^{d}
\frac{(-1)^\ell m^{(\ell)}(x)}{\ell!q^\ell}
(j+\sigma)^\ell
+o(q^{-d}).
\tag{14}
\]

Hence on the finite-support core the renormalized `d`-th packet tangent is simply

\[
\boxed{
q^d\left[
D_m-
\sum_{\ell=0}^{d-1}
\frac{(-1)^\ell m^{(\ell)}(x)}{\ell!q^\ell}J_\sigma^\ell
\right]
\longrightarrow
\frac{(-1)^dm^{(d)}(x)}{d!}J_\sigma^d.
}
\tag{15}
\]

In particular,

\[
\boxed{q(D_m-m(x)I)\longrightarrow -m'(x)J_\sigma}
\tag{16}
\]

on that core. Thus the subleading `1/q` information left open by PC-233 is not mysterious: its canonical tangent coordinate is ordinary lattice position.

## 4. The source Cauchy packet is outside every nontrivial tangent domain

Equation (16) must not be promoted to an operator limit on the actual source-forced packet without checking domains. From (2),

\[
J_\sigma f_\sigma(j)=C,
\tag{17}
\]

so

\[
\boxed{f_\sigma\in\ell^2(\mathbb Z)
\quad\text{but}\quad
f_\sigma\notin\operatorname{Dom}(J_\sigma).}
\tag{18}
\]

This gives a decisive obstruction to the most natural renormalized fixed-base repair. If `m'(x) != 0`, then the packet coordinates of

\[
q(D_m-m(x)I)T_{N,q}e_u
\tag{19}
\]

converge, for every fixed `j`, to the nonzero constant `-Cm'(x)`. For any fixed `J`, the squared norm restricted to `|j|<=J` therefore tends to

\[
(2J+1)|Cm'(x)|^2.
\tag{20}
\]

Since `J` is arbitrary,

\[
\boxed{
\left\|q(D_m-m(x)I)T_{N,q}e_u\right\|_2
\longrightarrow\infty
}
\tag{21}
\]

after projection to any nonzero packet sector with `m'(x) !=0`. No uniform-in-`j` Taylor estimate is needed for this conclusion; fixed-coordinate convergence plus arbitrarily large finite windows is enough.

The obstruction persists if the first nonzero derivative occurs at order `d>=1`. After subtracting all lower Taylor terms and multiplying by `q^d`, equation (15) gives on the packet

\[
J_\sigma^d f_\sigma(j)=C(j+\sigma)^{d-1},
\tag{22}
\]

which is never square-summable. Therefore every finite-order nonflat smooth tangent magnification sends the Cauchy packet out of its Hilbert space rather than producing a new bounded fixed-base spectral operator.

For the normalized inverse-square chord symbol of PC-233,

\[
m_{\rm ch}(x)=\frac{x(1-x)}2,
\tag{23}
\]

one has `m_ch'(x)=(1-2x)/2`. At the real frequency `x=1/2` the first tangent vanishes, but the second derivative is `-1`; the `q^2` correction is therefore proportional to `J_sigma^2` and has the same domain failure. The appearance of this half-frequency is only the elementary maximum of the regular-polygon dispersion. It supplies neither the complex symmetry `s <-> 1-s` nor a critical-line spectral condition.

## 5. Commutators cancel the bad tangent but give only the standard Laurent-shift algebra

The domain failure does not mean every fresh-scale operation diverges. Differences across a fixed fiber shift cancel the growing position factor. From (12), for fixed `h`,

\[
\begin{aligned}
[D_m,S_h]f(j)
=
&\left[
 m\!\left(x-\frac{j+\sigma}{q}\right)
-
 m\!\left(x-\frac{j+h+\sigma}{q}\right)
\right]f(j+h).
\end{aligned}
\tag{24}
\]

For `m in C^1`, multiplying by `q` and using the PC-227 `1/(1+|j|)` packet bound gives strong convergence on every packet:

\[
\boxed{
q[D_m,S_h]f_\sigma
\longrightarrow
h\,m'(x)S_hf_\sigma
\quad\text{in }\ell^2(\mathbb Z).
}
\tag{25}
\]

Indeed, the difference quotient converges uniformly on every fixed packet window and is uniformly bounded by `|h|\|m'\|_\infty`; the `ell^2` Cauchy tail then controls the complement. The same argument applies successively to finitely many smooth multipliers. For example,

\[
\boxed{
q^r\,\operatorname{ad}_{D_{m_1}}\cdots
\operatorname{ad}_{D_{m_r}}(S_h)f_\sigma
\longrightarrow
h^r\prod_{a=1}^r m_a'(x)\,S_hf_\sigma.
}
\tag{26}
\]

So canonical noncommutativity survives the fixed-base limit, but its entire leading content is a scalar derivative multiplying the same shift operator.

The position and shift obey

\[
\boxed{S J_\sigma=(J_\sigma+1)S,
\qquad [J_\sigma,S]=-S.}
\tag{27}
\]

Moreover

\[
J_\sigma=J_0+\sigma I.
\tag{28}
\]

Hence the cyclotomic packet shift `sigma` changes the position operator only by a central scalar. The noncommutative relation itself is independent of `N`, `q`, primality, the residue class, and the cyclotomic amplitude `C`. Fixed polynomial combinations of the tangent and fiber shift therefore lie in the ordinary Laurent-shift algebra

\[
\mathbb C[J]\langle S,S^{-1}\rangle/
\bigl(SJ-(J+1)S\bigr).
\tag{29}
\]

This is more structure than the purely abelian regular-`Z` channel classicalized in PC-206, but it is not new arithmetic structure: it is the standard discrete position/translation algebra.

## 6. Prior art and matched controls

The algebra in (27)--(29) is classical difference-operator/Heisenberg territory. A. Z. Górski and J. Szmigielski, **On Pairs of Difference Operators Satisfying: `[P,Q]=Id`**, *Journal of Mathematical Physics* 39 (1998), 545--568, DOI `10.1063/1.532322`, arXiv:hep-th/9703015, studies finite-difference realizations of the canonical commutation relation. Their **Representations of the Heisenberg algebra by difference operators**, *Acta Physica Polonica B* 31 (2000), 789--799, arXiv:hep-th/9808112, gives Hilbert-space shift realizations with discrete coordinate spectrum. Modern Laurent-shift work uses essentially the same algebraic presentation; for example Kyle Singh, **Fixed-Lowering sl2-Triples for Laurent-Shift Operators: Exact Stencil Endpoints and Recurrence Locality**, arXiv:2608.09962 (2026), works in `K[x]<S,S^{-1}>/(Sx-(x+1)S)`.

The RH-facing spectral warning is also established territory. Jens Bolte, Sebastian Egger and Stefan Keppeler, **The Berry-Keating operator on a lattice**, *Journal of Physics A* 50 (2017), 105201, DOI `10.1088/1751-8121/aa5844`, constructs a lattice difference-operator version of the Berry--Keating model by Weyl quantization on a torus. Thus taking the classical pair `(J,S)`, choosing a new Hamiltonian or boundary, and arranging an RH-looking spectrum would be an external spectral wrapper unless the prime-circle source itself forces that additional operator and its domain.

A matched nonarithmetic control is exact. Start with any shifted Cauchy sequence `C/(j+sigma)` with nonintegral `sigma`, with no cyclotomic interpretation. Integer translations, the chord difference (10), the tangent domain failure (17)--(22), the commutator limits (25)--(26), and the algebra (27)--(29) are unchanged. The only source-specific inputs are the finite list of rational shifts, amplitudes, and coarse samples already classified by PC-227--PC-234.

Accordingly, no novelty is claimed for Laurent shifts, discrete Heisenberg commutation, finite-difference tangents, or lattice spectralization. The project-specific result is the exact identification that the **first intrinsic fresh-fiber mode mixer and the first renormalized fixed-base frequency correction land precisely in that classical package**, with the naive tangent failing on the actual Cauchy packet domain.

## 7. Consequence for the live Prime-Circle frontier

PC-233 left mode mixing and renormalized fresh-scale structure open because a bounded macroscopic multiplier freezes to a coarse scalar. The most canonical representatives of both exits can now be removed:

\[
\boxed{
\begin{array}{c}
\text{fresh-fiber power-map coordinate}\ z^N
\\[2mm]
\text{or smooth }1/q\text{-scale multiplier tangent}
\end{array}
\quad\Longrightarrow\quad
\text{universal }(J,S)\text{ Laurent-shift calculus},
}
\tag{30}
\]

with an additional Hilbert-domain obstruction for the unsymmetrized tangent itself. The bounded commutator repair survives only as `h m'(x)S_h`; finite nested commutators do not create another arithmetic coordinate.

This is a fixed-base finite-operation boundary, not a global no-go. The following remain genuinely outside it:

- mode mixers forced by the complete old/new chord or cyclotomic geometry that are not fixed Laurent polynomials in the single fresh-fiber coordinate;
- shift support, polynomial degree, or operation depth growing with `q` strongly enough that the fixed Laurent algebra no longer controls the limit;
- singular or non-smooth multipliers whose variation is not represented by a finite Taylor jet;
- simultaneous `N,q -> infinity`, where both packet centers and fractional shifts become dynamical;
- operators coupling several packet sectors, several fresh primes, or amplitude/normalization data before reduction to one packet coordinate;
- global uniformization, accessory parameters, or another source-forced nonlinear geometry outside finite packet/difference calculus.

The remaining cross-prime search therefore has to create a state relation not generated by one packet's translation/position algebra. Merely resolving the `1/q` neighborhood of a fixed packet more finely, or replacing a frozen multiplier by its first finite Taylor jet, does not do so.