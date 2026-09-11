# PC-261 — prime triples realize zero and macroscopic defects at one resonant limit

**Status:** `LITERATURE+DERIVED` + `EXACT-DERIVED` + `DECISIVE-BOUNDARY` for the bounded-resonance part of the long shared-upper cocycle left after PC-258--PC-260.

Let

\[
D_{p,r;q}=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T},
\qquad
\Delta_{p,r;q}=\frac{D_{p,r;q}}{q\sqrt{pr}},
\tag{1}
\]

for distinct odd primes `p<r<q`. PC-253 identified two opposite congruence sectors: `q≡r (mod p)` forces `D=0`, while `q≡-r (mod p)` has an explicit collision rank and quadratic weight profile. Those sectors are not merely formal integer controls or isolated finite prime examples. There are **infinite all-prime sequences in both sectors**, and they can be chosen so that their PC-258 torus parameters converge to the **same** point

\[
\boxed{
\left(\frac pq,\frac rq\right)\longrightarrow
\left(\frac14,\frac12\right).
}
\tag{2}
\]

Along one sequence `Delta` vanishes identically. Along the other its rank is asymptotic to `2p/3` and

\[
\boxed{
\liminf \|\Delta_{p,r;q}\|_2\ge \frac1{\sqrt{540}}>0.
}
\tag{3}
\]

Thus the primitive long collision carrier has no ratio-only asymptotic at this resonant torus point, even after restricting to genuine prime triples. The missing datum is the **exact bounded integer resonance by which the rational orbit approaches the limiting point**. This does not produce a new RH mechanism: the existence of the two prime families is a direct instance of classical finite-complexity linear patterns in the primes, and the two operator behaviors are the already-classified rational-partition resonance sectors of PC-253.

## 1. The two resonance sectors contain arbitrarily large prime triples

The needed prime existence statement is an immediate application of Green--Tao's theorem on finite-complexity systems of affine-linear forms.

Consider first

\[
\Psi_-(x,y)=(x,\ y,\ y+2x).
\tag{4}
\]

The coefficient vectors `(1,0)`, `(0,1)`, and `(2,1)` are pairwise nonproportional, so the system has Cauchy--Schwarz complexity at most one. It is locally admissible. Modulo `2`, `(x,y)=(1,1)` makes all three forms nonzero. Modulo `3`, `(1,2)` does. For every prime `ell>=5`, the three forbidden zero sets are at most three lines in `F_ell^2`, so they cannot cover the plane. Hence the singular series is positive.

For any fixed `0<epsilon<1`, restrict `(x,y)` to a positive convex cone of the form

\[
N\le x\le 2N,
\qquad
(2-\epsilon)x<y<2x.
\tag{5}
\]

Green--Tao therefore gives prime points in (5) for arbitrarily large `N` with all three values in (4) prime. Choosing one such point for a sequence `epsilon_j -> 0` gives distinct primes

\[
p_j=x_j,
\qquad
r_j=y_j,
\qquad
q_j^-=y_j+2x_j,
\tag{6}
\]

with

\[
\frac{r_j}{p_j}\longrightarrow2
\quad\text{from below}.
\tag{7}
\]

The same argument applies to

\[
\Psi_+(x,y)=(x,\ y,\ 6x-y).
\tag{8}
\]

Again the three coefficient vectors are pairwise nonproportional and the system is locally admissible: modulo `2`, `(1,1)` works; modulo `3`, `(1,1)` works; and for primes `ell>=5` the union of the three zero lines is proper. Restrict now to

\[
N\le x\le 2N,
\qquad
2x<y<(2+\epsilon)x,
\qquad 0<\epsilon<1.
\tag{9}
\]

Then `6x-y>y>x`, so the simultaneous prime values give

\[
p_j=x_j,
\qquad
r_j=y_j,
\qquad
q_j^+=6x_j-y_j,
\tag{10}
\]

with `p_j<r_j<q_j^+` and

\[
\frac{r_j}{p_j}\longrightarrow2
\quad\text{from above}.
\tag{11}
\]

No unproved prime-gap or prime-tuple hypothesis is being used here. These are nondegenerate three-form systems in two variables, inside the unconditional finite-complexity regime of Green--Tao.

## 2. One all-prime sequence has exactly zero collision cocycle

For the family (6),

\[
q^- - r=2p,
\tag{12}
\]

so

\[
q^-\equiv r\pmod p.
\tag{13}
\]

PC-253 proves that this congruence forces the shared-upper defect to vanish exactly:

\[
\boxed{
D_{p,r;q^-}=0,
\qquad
\Delta_{p,r;q^-}=0.
}
\tag{14}
\]

Thus the complete PC-257 transfer object is absent, not merely small after normalization. This gives arbitrarily large genuine prime triples in a comparable-scale regime with collision rank zero.

Writing `gamma=r/p`, the torus parameters of PC-258 are

\[
\alpha_-:=\frac{p}{q^-}=\frac1{\gamma+2},
\qquad
\beta_-:=\frac{r}{q^-}=\frac{\gamma}{\gamma+2}.
\tag{15}
\]

Equation (7) therefore gives

\[
(\alpha_-,\beta_-)\longrightarrow(1/4,1/2).
\tag{16}
\]

At every finite level this family lies on the exact bounded resonance

\[
\boxed{2\alpha_-+\beta_-=1.}
\tag{17}
\]

## 3. The second all-prime sequence has macroscopic collision rank

For the family (10),

\[
q^+ + r=6p,
\tag{18}
\]

so

\[
q^+\equiv-r\pmod p.
\tag{19}
\]

This is the opposite PC-253 sector with `m=6`. Put

\[
H=\left\lfloor\frac{pr-1}{q^++r}\right\rfloor
=
\left\lfloor\frac{pr-1}{6p}\right\rfloor.
\tag{20}
\]

PC-253 gives

\[
\boxed{
\operatorname{rank}D_{p,r;q^+}=2H,
}
\tag{21}
\]

and the positive determinant-layer weights

\[
\boxed{
w_h=h(r-6h),\qquad1\le h\le H,}
\tag{22}
\]

with the reflected negative layers carrying the same weights. Since `r/p -> 2`,

\[
\frac{H}{r}\longrightarrow\frac16,
\qquad
\boxed{
\frac{\operatorname{rank}D_{p,r;q^+}}p
\longrightarrow\frac23.
}
\tag{23}
\]

Hence this is a genuinely depth-growing PC-257/PC-260 collision chain, not a fixed-rank exceptional packet.

Its torus parameters are

\[
\alpha_+:=\frac{p}{q^+}=\frac1{6-\gamma},
\qquad
\beta_+:=\frac{r}{q^+}=\frac{\gamma}{6-\gamma},
\tag{24}
\]

so (11) gives the same limit

\[
(\alpha_+,\beta_+)\longrightarrow(1/4,1/2).
\tag{25}
\]

At every finite level, however, this family lies on the distinct exact resonance

\[
\boxed{6\alpha_+-\beta_+=1.}
\tag{26}
\]

The limiting point `(1/4,1/2)` lies on both resonance lines (17) and (26). The finite arithmetic lift, not the limiting torus point alone, determines which collision sector is realized.

## 4. The opposite-sign family survives native normalization

Rank growth alone would not be enough: the complete defect could still vanish after the native normalization (1). Here it does not.

PC-251 writes `D` as a sum of weighted `2 x 2` path-incidence tiles. Each tile of weight `w` has squared Frobenius norm `4w^2`. PC-257 shows that when consecutive tiles overlap in a matrix entry, their contributions have the same sign, so overlap cannot lower the squared Frobenius norm. Using the reflected equality of the positive and negative determinant-layer weights,

\[
\|D_{p,r;q^+}\|_F^2
\ge
8\sum_{h=1}^{H} h^2(r-6h)^2.
\tag{27}
\]

Because `H/r -> 1/6`, the Riemann sum is exact at leading order:

\[
\frac1{r^5}
\sum_{h=1}^{H} h^2(r-6h)^2
\longrightarrow
\int_0^{1/6}t^2(1-6t)^2\,dt
=
\frac1{6480}.
\tag{28}
\]

Together with `rank D=2H` and the elementary inequality

\[
\|D\|_2^2\ge
\frac{\|D\|_F^2}{\operatorname{rank}D},
\tag{29}
\]

this gives

\[
\boxed{
\liminf
\frac{\|D_{p,r;q^+}\|_2}{r^2}
\ge
\frac1{\sqrt{270}}.
}
\tag{30}
\]

Finally, with `gamma=r/p -> 2`,

\[
\frac{r^2}{q^+\sqrt{pr}}
=
\frac{\gamma^{3/2}}{6-\gamma}
\longrightarrow
\frac1{\sqrt2}.
\tag{31}
\]

Combining (30)--(31) proves the normalized lower bound (3):

\[
\boxed{
\liminf\|\Delta_{p,r;q^+}\|_2
\ge
\frac1{\sqrt{540}}.
}
\tag{32}
\]

Thus the contrast with (14) survives exactly at the normalization already selected by the Prime-Circle overlap geometry.

## 5. Finite controls

The zero family is already visible at

\[
(p,r,q)=(47,97,191),
\]

where `q-r=94=2p`; PC-253 therefore gives `D=0` exactly.

For the opposite family,

\[
(p,r,q)=(29,61,113)
\]

has `q+r=174=6p`. Equation (20) gives `H=10`, hence rank `20`, and the positive collision weights from (22) are

\[
55,98,129,148,155,150,133,104,63,10,
\]

with the same ten weights on the reflected negative layers. These examples are only finite sanity checks; the infinite-family statement comes from the linear-forms theorem in Section 1.

## 6. Prior art and novelty audit

The prime-existence input is classical modern additive number theory, not a new Prime-Circle theorem. The primary source is:

- Ben Green and Terence Tao, **Linear equations in primes**, *Annals of Mathematics* 171:3 (2010), 1753--1850, DOI `10.4007/annals.2010.171.1753`, arXiv:`math/0606088`. Their theorem counts simultaneous prime values of nondegenerate finite-complexity affine-linear systems in convex regions; the complexity-one systems (4) and (8) lie in their unconditional range.

The mechanical-word/torus side is likewise already classicalized by PC-258, and the exact zero/opposite collision formulas are PC-253. No novelty is claimed for Green--Tao prime patterns, rational torus resonances, mechanical words, congruence sectors, or the Frobenius/spectral-norm inequality.

The durable project-local consequence is the **combination** of those facts: the extreme resonance sectors of PC-253 occur infinitely often inside the actual all-prime source, and two such prime sequences can approach the same PC-258 torus parameter while their natively normalized complete defects have incompatible limits. This closes a logical gap left by treating the PC-253 sectors merely as algebraic possibilities or finite examples.

A search around prime values of linear forms, Beatty/mechanical-word intersections, and rational torus codings found the expected classical theories, but no reason to reinterpret this consequence as a new zeta-specific spectral mechanism. The result does not rely on an absence-of-literature claim.

## 7. Boundaries and falsification

This finding is deliberately restricted to the bounded-resonance boundary excluded from the Haar/nonresonant limit in PC-258. It does **not** show that two nonresonant prime sequences with the same irrational limiting `(alpha,beta)` can have different limiting Lyapunov or spectral data. It also does not rule out an observable that retains the exact resonance vector as part of its state. What it rules out is stronger than a finite counterexample but narrower than a global no-go:

\[
\boxed{
\text{all-prime} + \text{comparable scales} +
(\alpha_n,\beta_n)\to(\alpha,\beta)
}
\]

is insufficient to determine even whether the normalized shared-upper cocycle vanishes at a resonant limit point.

The theorem can be falsified in three independent places:

1. show that either linear-form system (4) or (8) fails finite-complexity admissibility in the stated convex cones;
2. produce a prime triple in (12) or (18) violating the exact PC-253 congruence-sector formulas;
3. find cancellation between overlapping PC-251 incidence tiles that invalidates (27), contrary to the same-sign overlap proved in PC-257.

Absent one of those failures, (14), (23), and (32) are exact/literature-derived consequences.

## 8. Consequence for the live Prime-Circle frontier

PC-258 left long return/cocycle information open after every fixed local window classicalized, PC-259 removed common-dilation fake depth, and PC-260 imposed exact reversal parity. PC-261 now separates the **resonant** part of that frontier from the genuinely nonresonant one.

Bounded resonance is real inside the prime source and can change the complete normalized operator by `O(1)`, but its occurrence already belongs to classical affine-linear prime-pattern theory. In particular, a universal cofinal lower bound for the PC-251 defect over all comparable prime triples is impossible, while a nonzero resonance subsector is not by itself evidence for a zeta-zero mechanism.

The sharper surviving question is therefore: after conditioning away exact bounded resonances, can a primitive parity-reduced depth-growing cocycle in a nonresonant regime retain a source-specific invariant that is not determined by classical rational-torus dynamics or by the way primes sample ordinary affine-linear patterns? PC-261 does not answer that nonresonant question.