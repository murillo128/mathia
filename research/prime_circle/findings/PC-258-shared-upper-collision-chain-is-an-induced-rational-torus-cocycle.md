# PC-258 — shared-upper collision chain is an induced rational-torus cocycle

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the growing-length fixed-width transfer escape left open by PC-257. Fix distinct primes

\[
2<p<r<q,
\qquad
\alpha=\frac pq,
\qquad
\beta=\frac rq.
\tag{1}
\]

PC-251 identifies the shared-upper defect

\[
D_{p,r;q}=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T}
\]

as a monotone weighted collision matching, and PC-257 shows that its complete singular-spectrum problem is a width-two transfer chain whose local input is the ordered word of collision weights and adjacency bits. That surviving word is not free combinatorial data. It is exactly the return coding of the rational torus translation

\[
T_{\alpha,\beta}(x,y)=(x+\alpha,y+\beta)\pmod1
\tag{2}
\]

to the rectangle

\[
W_{\alpha,\beta}=[1-\alpha,1)\times[1-\beta,1).
\tag{3}
\]

More precisely, the complete PC-257 input `((w_a),(epsilon_a),(eta_a))` is reconstructed from successive returns of the orbit of `(0,0)` to (3), including the exact Green-kernel weights. In nonresonant simultaneous-growth limits this orbit equidistributes on the two-torus, the collision density tends to `alpha beta`, and the native normalized collision weights have the universal limiting law

\[
\boxed{
\rho
\ \Longrightarrow\ 
\sqrt{\alpha\beta}\,G(U,V),
\qquad
G(u,v)=\min(u,v)-uv,
}
\tag{4}
\]

where `U,V` are independent uniform variables on `[0,1]`. Hence every fixed local window of the collision coding has a classical torus-translation limit. The only part of the PC-257 transfer problem not classicalized by this result is genuinely long-range return/cocycle information whose observation depth grows with `q` or with the collision rank.

## 1. Each lower partition is a rational mechanical word

For `0<=u<=q-2` define the boundary indicators

\[
b_p(u)=
\left\lfloor\frac{p(u+1)}q\right\rfloor-
\left\lfloor\frac{pu}q\right\rfloor,
\tag{5}
\]

\[
b_r(u)=
\left\lfloor\frac{r(u+1)}q\right\rfloor-
\left\lfloor\frac{ru}q\right\rfloor.
\tag{6}
\]

Because `p,r<q`, both take only the values `0,1`. They record whether the common upper cell `[u,u+1)` contains an interior boundary of the `p`- or `r`-partition used in PC-251.

Put

\[
\theta_u=\{u\alpha\},
\qquad
\phi_u=\{u\beta\}.
\tag{7}
\]

The elementary mechanical-word identity

\[
\lfloor x+t\rfloor-\lfloor x\rfloor=1
\iff
\{x\}\ge1-t,
\qquad 0<t<1,
\]

gives

\[
\boxed{
b_p(u)=1\iff\theta_u\in[1-\alpha,1),}
\tag{8}
\]

\[
\boxed{
b_r(u)=1\iff\phi_u\in[1-\beta,1).}
\tag{9}
\]

Therefore an upper cell is a PC-251 double-boundary collision cell exactly when

\[
\boxed{
T_{\alpha,\beta}^{u}(0,0)
=(\theta_u,\phi_u)
\in W_{\alpha,\beta}.
}
\tag{10}
\]

If (10) holds, the corresponding lower boundary indices are

\[
i_u=\left\lfloor\alpha(u+1)\right\rfloor,
\qquad
j_u=\left\lfloor\beta(u+1)\right\rfloor.
\tag{11}
\]

They satisfy

\[
\left\lfloor\frac{q i_u}{p}\right\rfloor
=
\left\lfloor\frac{q j_u}{r}\right\rfloor=u,
\tag{12}
\]

so (10)--(12) are exactly the collision set of PC-251, not an asymptotic surrogate. As `u` increases, both indices increase, so the return-time ordering is exactly the monotone collision ordering used in PC-254--PC-257.

The two rational binary sequences (5)--(6) are standard rational mechanical/Christoffel codings. Their intersection is therefore most naturally viewed as a coding of the product rotation (2), rather than as a new prime-specific symbolic system.

## 2. The Green-kernel weight is an explicit torus observable

Suppose `u` is a collision cell. The `p`-boundary lies inside that unit cell at the fractional coordinate

\[
\xi_u
=\frac{q i_u}{p}-u.
\tag{13}
\]

Using (7), (8), and `i_u=floor(alpha u)+1`, one obtains

\[
\boxed{
\xi_u=\frac{1-\theta_u}{\alpha}.
}
\tag{14}
\]

Likewise

\[
\boxed{
\upsilon_u=\frac{1-\phi_u}{\beta}.
}
\tag{15}
\]

Both coordinates lie strictly in `(0,1)` for interior collision cells. PC-251 gives the exact integer collision weight

\[
w_u=pr\,G(\xi_u,\upsilon_u),
\qquad
G(x,y)=\min(x,y)-xy.
\tag{16}
\]

For the native normalization

\[
\Delta_{p,r;q}=
\frac{D_{p,r;q}}{q\sqrt{pr}},
\tag{17}
\]

the coefficient attached to the collision is therefore

\[
\boxed{
\rho_u
:=\frac{w_u}{q\sqrt{pr}}
=
\sqrt{\alpha\beta}\,
G\!\left(
\frac{1-\theta_u}{\alpha},
\frac{1-\phi_u}{\beta}
\right).
}
\tag{18}
\]

Thus even the exact PC-251 weight is a fixed bounded observable sampled at torus return points. No additional arithmetic label is hidden in the weight after the normalized ratios and orbit point are known.

## 3. The PC-257 adjacency bits are return-path observables

Let

\[
u_1<u_2<\cdots<u_k
\]

be the successive collision cells. PC-257 defines

\[
\varepsilon_a=
\mathbf 1_{\{i_{u_{a+1}}=i_{u_a}+1\}},
\qquad
\eta_a=
\mathbf 1_{\{j_{u_{a+1}}=j_{u_a}+1\}}.
\tag{19}
\]

Telescoping (5) gives

\[
i_{u_{a+1}}-i_{u_a}
=
\sum_{v=u_a+1}^{u_{a+1}} b_p(v),
\tag{20}
\]

and similarly

\[
j_{u_{a+1}}-j_{u_a}
=
\sum_{v=u_a+1}^{u_{a+1}} b_r(v).
\tag{21}
\]

Consequently

\[
\boxed{
\varepsilon_a=1
\iff
\sum_{v=u_a+1}^{u_{a+1}} b_p(v)=1,
}
\tag{22}
\]

\[
\boxed{
\eta_a=1
\iff
\sum_{v=u_a+1}^{u_{a+1}} b_r(v)=1.
}
\tag{23}
\]

Equations (18), (22), and (23) show that the **entire** weighted binary collision word used by the width-two transfer recursion in PC-257 is an induced-return observable of the single rational torus translation (2). There is no independent matrix-combinatorial degree of freedom left after the source-forced rational-partition reduction.

This does not make the growing transfer product trivial. A long matrix cocycle over a rotation can have nontrivial global dynamics. It does identify the exact base system that must carry any surviving information: the first-return process of (2) to (3), together with the explicit observable (18).

## 4. Nonresonant simultaneous growth gives Haar torus statistics

Consider any sequence of prime triples

\[
(p_n,r_n,q_n),
\qquad q_n\to\infty,
\]

with

\[
\alpha_n=\frac{p_n}{q_n}\to\alpha,
\qquad
\beta_n=\frac{r_n}{q_n}\to\beta,
\qquad
0<\alpha<\beta<1.
\tag{24}
\]

Assume the sequence is **bounded-mode nonresonant**: for every fixed `(h,k) in Z^2\setminus{(0,0)}`,

\[
q_n\nmid h p_n+k r_n
\tag{25}
\]

for all sufficiently large `n`. A sufficient, but not necessary, condition is that `1,alpha,beta` are linearly independent over `Q`.

Let

\[
\mu_n=
\frac1{q_n}
\sum_{u=0}^{q_n-1}
\delta_{(\{up_n/q_n\},\{ur_n/q_n\})}.
\tag{26}
\]

For a Fourier mode `(h,k)`, the exact finite geometric sum is

\[
\widehat\mu_n(h,k)
=
\frac1{q_n}
\sum_{u=0}^{q_n-1}
\exp\!\left(
\frac{2\pi i u(hp_n+kr_n)}{q_n}
\right)
=
\begin{cases}
1,&q_n\mid hp_n+kr_n,\\
0,&\text{otherwise}.
\end{cases}
\tag{27}
\]

Hence (25) makes every fixed nonzero Fourier coefficient eventually vanish. By the Weyl criterion,

\[
\boxed{
\mu_n\Longrightarrow m_{\mathbb T^2},
}
\tag{28}
\]

where `m_{T^2}` is Haar probability measure on the two-torus.

The boundary of `W_{alpha,beta}` has Haar measure zero, so (28) immediately yields the collision-density law

\[
\boxed{
\frac{k_n}{q_n}\longrightarrow\alpha\beta.
}
\tag{29}
\]

This is the generic bulk counterpart of the moving congruence-lattice discrepancy in PC-253.

Condition on a collision. Haar measure restricted to (3) makes `theta` and `phi` independent uniforms on their two interval factors. The affine changes

\[
U=\frac{1-\theta}{\alpha},
\qquad
V=\frac{1-\phi}{\beta}
\tag{30}
\]

therefore make `U,V` independent uniforms on `[0,1]`. Combining (18), (28), and (30) proves the weight law (4).

All positive integer moments are consequently explicit:

\[
\boxed{
\lim_{n\to\infty}
\frac1{k_n}
\sum_{a=1}^{k_n}\rho_{n,a}^{m}
=
(\alpha\beta)^{m/2}
\frac{2(m!)^2}{(2m+2)!}.
}
\tag{31}
\]

Indeed, on the triangle `0<u<v<1`, `G(u,v)=u(1-v)`, so symmetry gives

\[
\mathbb E[G(U,V)^m]
=2\int_0^1\int_u^1u^m(1-v)^m\,dv\,du
=
\frac{2(m!)^2}{(2m+2)!}.
\tag{32}
\]

For example,

\[
\mathbb E\rho
=\frac{\sqrt{\alpha\beta}}{12},
\qquad
\mathbb E\rho^2
=\frac{\alpha\beta}{90}.
\tag{33}
\]

Thus the generic normalized local weight packet has a universal continuous law up to the elementary scale `sqrt(alpha beta)`.

## 5. Every fixed raw-cell window has a classical torus limit

The same argument is not restricted to one-point weights. Fix a raw upper-cell window length `L`. The finite pattern

\[
\bigl(
 b_p(u+t),b_r(u+t)
\bigr)_{0\le t\le L}
\tag{34}
\]

is determined by the initial torus point `(theta_u,phi_u)` and membership in finitely many translates of the intervals in (8)--(9). Any bounded local statistic built from (34) and the cut-position observables (14)--(15) is therefore a bounded piecewise-continuous function on `T^2` whose discontinuity set is a finite union of line segments.

Under the nonresonance hypothesis (25), its empirical average converges by (28) to the corresponding Haar integral. Pattern frequencies reduce to areas of finite intersections of translated rectangles; weighted pattern averages reduce to ordinary integrals of the explicit Green observable over those polygons.

Hence no statistic that observes only a **fixed number of raw upper cells** can retain a new prime-specific asymptotic packet in this regime. This is the dynamical analogue of the fixed-depth classicalizations in PC-255--PC-256. It leaves open only observation depth or return-cocycle length growing with the collision rank.

## 6. PC-253's extreme orientation sectors are bounded torus resonances

The exact congruence sectors of PC-253 fit naturally into (27). If

\[
q\equiv r\pmod p,
\]
write

\[
q-r=mp.
\tag{35}
\]

Then

\[
m\alpha+\beta=1,
\tag{36}
\]

and the Fourier mode `(m,1)` in (27) is identically resonant. PC-253 proves that in this sector the collision defect vanishes exactly.

If instead

\[
q\equiv-r\pmod p,
\]
write

\[
q+r=mp.
\tag{37}
\]

Then

\[
m\alpha-\beta=1,
\tag{38}
\]

and the mode `(m,-1)` is identically resonant; PC-253 gives the resulting macroscopic collision family and its quadratic weights explicitly.

Thus the sharp orientation effects found in PC-253 are not separate mysterious exceptions to the generic collision geometry. They are low-complexity rational resonances of the same torus coding. In the comparable-scale regime `m` is bounded, so any infinite family in one of these sectors has a subsequence with a fixed resonant Fourier mode.

The distinction matters for future asymptotics. A statement proved only in a Haar/nonresonant scaling limit cannot be extrapolated to the resonant arithmetic sectors, while a signal confined to one bounded resonance must be compared against the corresponding classical lower-dimensional torus dynamics before it is treated as new Prime-Circle information.

## 7. Exact control at `(p,r,q)=(7,11,13)`

Here

\[
\alpha=\frac7{13},
\qquad
\beta=\frac{11}{13}.
\]

Equations (8)--(10) give the six interior double-boundary return cells

\[
 u=1,3,5,7,9,11.
\tag{39}
\]

Equation (11) gives the collision pairs

\[
(1,1),(2,3),(3,5),(4,6),(5,8),(6,10),
\tag{40}
\]

and (16) gives the weights

\[
2,12,4,4,12,2.
\tag{41}
\]

These are exactly the collision data used independently in PC-254 and PC-257. The present representation therefore reproduces both the ordered support and the full local weight packet, not merely its rank or moments.

## 8. Prior-art and novelty audit

The dynamical ingredients are classical. Rational mechanical words and their irrational Sturmian limits are standard codings of circle rotations; see M. Lothaire, **Algebraic Combinatorics on Words**, Chapter 2, *Sturmian Words*, Cambridge University Press (2002), DOI `10.1017/CBO9781107326019.003`. Coding translations of the two-dimensional torus is likewise an established symbolic-dynamics subject; a directly adjacent reference is Nicolas Chevallier, **Coding of a translation of the two-dimensional torus**, *Monatshefte für Mathematik* 157 (2009), 101--130, DOI `10.1007/s00605-008-0074-y`. Intersections of Beatty/mechanical sequences are also classical objects; see, for example, A. V. Begunts and D. V. Goryashin, **On the intersection of two homogeneous Beatty sequences**, *Chebyshevskii Sbornik* 23:5 (2022/2023), 145--151, DOI `10.22405/2226-8383-2022-23-5-145-151`.

The equidistribution step is a direct finite Fourier application of Hermann Weyl's classical criterion; see H. Weyl, **Über die Gleichverteilung von Zahlen mod. Eins**, *Mathematische Annalen* 77 (1916), 313--352, DOI `10.1007/BF01475864`, and L. Kuipers and H. Niederreiter, **Uniform Distribution of Sequences**, Wiley (1974; Dover reprint 2006).

No novelty is claimed for mechanical words, Christoffel/Sturmian coding, torus translations, Beatty intersections, first-return codings, or Weyl equidistribution. The project-local result is the exact identification (10), (18), and (22)--(23) for the **source-forced PC-251 collision defect**, followed by the generic limit (29)--(33). This identifies the full base dynamics of the growing transfer carrier left open by PC-257.

The matched-control result remains negative for prime specificity. PC-251 already shows that the same uniform rational-partition collision construction is reproduced by admissible pairwise-coprime non-prime controls. Every equation above after the packet construction uses only the rational slopes `p/q`, `r/q`, floor increments, and the Green kernel. Therefore the torus-return system and its generic Haar limit are source-blind once those partition ratios are supplied.

A targeted prior-art search found extensive classical theory for rotation coding, torus translations, Beatty intersections, and equidistribution, but no reason to interpret this exact Prime-Circle specialization as a new zeta operator. The conclusion does not rely on an absence-of-literature novelty claim.

## 9. RH-facing consequence and surviving boundary

PC-257 reduced the complete shared-upper spectrum to a fixed-width transfer product of growing length but left open whether the long cocycle could retain qualitatively new arithmetic information. PC-258 now identifies the source of that cocycle exactly: it is an induced cocycle over a rational two-torus translation, and in bounded-mode nonresonant simultaneous-growth limits all fixed local statistics converge to classical Haar-torus integrals. The normalized scalar weight law is universal in the strong sense of (31).

This is a **boundary theorem, not an RH no-go**. A Lyapunov exponent, discriminant, rotation number, winding invariant, or another genuinely global observable of a length-growing return cocycle can still depend on long-range ordering not captured by any fixed window. Exceptional bounded-resonance sectors can also differ sharply from the Haar regime, as PC-253 already proves. What is closed is the interpretation that the PC-257 long chain carries an unexplained prime-specific local alphabet or local weight distribution.

Any surviving RH proposal based on this branch must now do all of the following: use a cocycle observable whose depth grows with the return chain; distinguish the actual cyclotomic/prime source from the matched rational-partition control; specify whether it uses a nonresonant or resonant scaling topology; and derive rather than import the complex parameter, functional equation, explicit-formula term, or critical normalization. Neither the mechanical-word coding nor Haar equidistribution supplies such a bridge by itself.

In particular, no `s`-variable, gamma factor, `s<->1-s` symmetry, zeta zero divisor, or critical-line normalization appears in (2)--(38). The next live question is therefore no longer whether the full shared-upper collision spectrum is high-dimensional or locally exotic. It is whether a **global, growing-length matrix cocycle over this explicit torus-return system** has a source-forced invariant that survives the matched controls and connects nontrivially to zeta.

## 10. Exact falsification audit

The finite theorem can be falsified without asymptotics. For any proposed prime triple, compute (5)--(6), list the cells where both indicators equal one, and verify that (11) reproduces the PC-251 collision pairs in the same order. On each such cell, compare the native PC-251 integer weight against (16). Then compare the PC-257 adjacency bits against the Birkhoff-sum criteria (22)--(23). A failure of any one of these identities falsifies the torus-return representation.

For a proposed nonresonant scaling family, test the exact divisibility condition (25) for each fixed Fourier mode under consideration. The Haar conclusion is justified only after bounded-mode resonances disappear. Once that gate is satisfied, collision density, normalized weight moments, and every fixed-window statistic must converge to (29)--(33) and the corresponding Haar polygon integrals. A persistent discrepancy would falsify the asymptotic part of the finding.
