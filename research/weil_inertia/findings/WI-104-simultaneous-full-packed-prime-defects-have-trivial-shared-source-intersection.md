# WI-104 — Simultaneous full-packed prime defects have trivial shared-source intersection

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It resolves the source-labelled consistency question left open by WI-102 and `CLUE-full-packing-orbit-quotient-characters`: two distinct positive-defect fully packed residual prime interactions that share one source prime at the same observation length cannot reuse any nonzero source-kernel direction. Equivalently, concatenating the two target cross Grams restores full source row rank.

There is also a necessary coordinate correction to the earlier exploratory picture. The canonical short-boundary models for two pairs can have deleted-interval centers that are equal or opposite modulo `p`, but when the nearest boundary comes from the **complement** of a pairwise period, the actual cross Gram carries a source-side diagonal phase. In the `p`-residue row-kernel coordinates this phase is a translation. After restoring it, all simultaneous full-packed kernels at one actual observation length have the **same** deleted-interval center. Thus the actual shared-source geometry is concentric, not a mixture of concentric and antipodal holes.

Let `p` be an odd prime and let `q_1,q_2` be distinct odd primes with

\[
p<q_i<2p.
\tag{1}
\]

For one observation length `N`, write

\[
r_i=N\bmod p q_i,
\qquad
\delta_i=\min\{r_i,pq_i-r_i\},
\tag{2}
\]

and let

\[
\varepsilon_i=
\begin{cases}
+1,&r_i=\delta_i,\\
-1,&r_i=pq_i-\delta_i.
\end{cases}
\tag{3}
\]

(The moduli are odd, so the two cases do not tie away from `delta_i=0`; the positive-defect regime below excludes `delta_i=0`.) Assume that each `delta_i` lies in the genuinely residual **full-packing** regime of WI-096/WI-102. Thus, with

\[
d_i=q_i-p,
\qquad
t_i=p-d_i=2p-q_i,
\tag{4}
\]

we may write

\[
\delta_i=k_iq_i+s_i,
\qquad
R_i=s_i-d_i=[k_i d_i]_p,
\qquad
0<R_i<t_i,
\tag{5}
\]

and full packing gives the canonical deleted interval

\[
C_i^{\rm can}=\{R_i,\ldots,R_i+d_i-1\}.
\tag{6}
\]

Put

\[
g_i=\gcd(R_i,t_i),
\tag{7}
\]

and assume positive defect, equivalently `g_i>1`; WI-102 then gives canonical defect `g_i-1`.

Let

\[
G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\qquad
K_i=\ker_{\rm left}G_i
\subset \mathbf C^{p-1}.
\tag{8}
\]

Then

\[
\boxed{K_1\cap K_2=\{0\}.}
\tag{9}
\]

Consequently the horizontally concatenated cross Gram has full source row rank:

\[
\boxed{
\operatorname{rank}\,[G_1\;G_2]=p-1.
}
\tag{10}
\]

The proof is exact. Its only external theorem is the classical Fine--Wilf periodicity theorem for a finite word with two periods.

## 1. The complement boundary translates the actual source kernel

For primitive frequencies `a mod p`, `b mod q`, put

\[
z_{a,b}=e(b/q-a/p).
\tag{11}
\]

If `r_i=delta_i`, complete `pq_i` periods cancel and the actual cross Gram is the canonical short block of length `delta_i`. If instead

\[
r_i=pq_i-\delta_i,
\tag{12}
\]

then, because `z_{a,b}^{pq_i}=1`,

\[
\sum_{x=0}^{pq_i-\delta_i-1}z_{a,b}^x
=-z_{a,b}^{-\delta_i}\sum_{u=0}^{\delta_i-1}z_{a,b}^u.
\tag{13}
\]

Hence

\[
G_i^{(N)}
=-D_p(\delta_i)\,G_i^{(\delta_i)}\,D_{q_i}(-\delta_i),
\tag{14}
\]

where the source diagonal has entries

\[
D_p(\delta_i)_{a,a}=e(a\delta_i/p).
\tag{15}
\]

Represent a row dependence `lambda=(lambda_a)` by the `p`-periodic zero-mean function

\[
f(j)=\sum_{a=1}^{p-1}\lambda_a e(-aj/p).
\tag{16}
\]

Equation (14) says that in the complement case the actual row dependence is obtained from a canonical one `mu` by

\[
\lambda_a=\mu_a e(-a\delta_i/p),
\tag{17}
\]

and therefore

\[
f_{\rm actual}(j)=f_{\rm can}(j+\delta_i).
\tag{18}
\]

Thus the canonical source-residue kernel must be translated by `-delta_i` before kernels from different target moduli are compared in one shared source coordinate system. This phase is irrelevant to pairwise rank, which is why it did not appear in WI-081--WI-102, but it is load-bearing for simultaneous kernel intersections.

Full packing gives

\[
\delta_i\equiv k_i d_i+s_i
\equiv R_i+(R_i+d_i)
=2R_i+d_i
\pmod p.
\tag{19}
\]

Define the actual deleted-interval start

\[
\rho_i=
\begin{cases}
R_i,&\varepsilon_i=+1,\\
t_i-R_i,&\varepsilon_i=-1.
\end{cases}
\tag{20}
\]

For `epsilon_i=-1`, translating (6) by `-delta_i` changes its start to

\[
R_i-\delta_i
\equiv -R_i-d_i
\equiv p-R_i-d_i
=t_i-R_i=\rho_i
\pmod p.
\tag{21}
\]

Since `0<R_i<t_i`, both cases satisfy

\[
0<\rho_i<t_i,
\qquad
0<\rho_i+d_i<p.
\tag{22}
\]

The actual forced-zero interval is therefore the ordinary interval

\[
\boxed{
C_i=\{\rho_i,\ldots,\rho_i+d_i-1\}.
}
\tag{23}
\]

Moreover

\[
\gcd(\rho_i,t_i)=\gcd(R_i,t_i)=g_i.
\tag{24}
\]

## 2. All actual holes at one source and one observation length are concentric

Because `p,q_i` are odd, `d_i` is even. Define the integer center parameter

\[
c_i=\rho_i+\frac{d_i}{2}.
\tag{25}
\]

For `epsilon_i=+1`, equations (19)--(20) give

\[
2c_i=2R_i+d_i\equiv\delta_i\equiv N\pmod p.
\tag{26}
\]

For `epsilon_i=-1`,

\[
2c_i
=2(t_i-R_i)+d_i
=2p-(2R_i+d_i)
\equiv-\delta_i
\equiv N
\pmod p.
\tag{27}
\]

Every actual center satisfies `0<c_i<p`. Since `2` is invertible modulo the odd prime `p`, (26)--(27) force

\[
\boxed{c_1=c_2=:c.}
\tag{28}
\]

Thus the actual holes are concentric. If `d_1<d_2`, then

\[
C_1\subsetneq C_2.
\tag{29}
\]

The earlier equal-or-opposite center law applies to the **unsigned canonical short-boundary charts** before the source diagonal phase in (14) is restored. For shared-source kernel intersections, (28) is the correct invariant statement.

## 3. A fully packed row kernel is the augmentation ideal of one cyclic quotient

The quotient-character normal form proposed in the clue is exact. Fix one pair and suppress the index. WI-102 collapses the canonical hole and conjugates the free permutation to rotation by `R` on `Z/tZ`; WI-096 identifies the true row kernel with functions that vanish on the deleted interval, are constant on the free cycles, and have zero mean.

The same description holds for the actual start `rho` after the translation in Section 1. Unwrap the complement of the actual hole by assigning to every source residue outside `C` its unique integer representative in

\[
\boxed{
I=[\rho-t,\rho-1].
}
\tag{30}
\]

This interval has exactly `t` integers. In the `epsilon=+1` chart, WI-102's collapse map is `j` below the hole and `j-d` above it. Since `g` divides `t=p-d`, the orbit label modulo `g` is exactly the unwrapped integer `w mod g`. In the complement chart, (18) translates the canonical interval to (30); the lift differs from the canonical lift by

\[
2R-t,
\tag{31}
\]

which is divisible by `g`, so the same residue label `w mod g` results.

Consequently every actual full-packed kernel vector has the exact form

\[
f(j)=0\quad(j\in C),
\tag{32}
\]

and, for `w in I` with `j=w mod p`,

\[
\boxed{
f(j)=F(w\bmod g)
}
\tag{33}
\]

for a function `F:Z/gZ -> C`. Since `g|t`, every quotient residue occurs exactly `t/g` times in `I`; the source zero-mean condition is therefore

\[
\boxed{
\sum_{x\bmod g}F(x)=0.
}
\tag{34}
\]

Hence

\[
\boxed{
K\simeq
\left\{F:\mathbf Z/g\mathbf Z\to\mathbf C:
\sum_xF(x)=0\right\}.
}
\tag{35}
\]

This is the augmentation hyperplane of the regular representation of the cyclic quotient

\[
Q=(\mathbf Z/t\mathbf Z)/\langle\rho\rangle
\simeq\mathbf Z/g\mathbf Z.
\tag{36}
\]

In particular the nontrivial characters of `Z/gZ` give an explicit basis: for `1<=a<g`, set `f=0` on `C` and

\[
f(w\bmod p)=e(aw/g)
\qquad(w\in I).
\tag{37}
\]

Thus the character normal form suggested by the WI-102 Lean quotient is not merely a change of language; it supplies the periodic coordinates used in the simultaneous proof below.

## 4. Two concentric full-packed kernels reduce to a Fine--Wilf word

Order the targets so that

\[
d_1<d_2
\tag{38}
\]

and put

\[
h_i=d_i/2,
\qquad
r=h_2-h_1>0.
\tag{39}
\]

Since `rho_i=c-h_i` and `t_i=p-2h_i`, their unwrapped complement intervals are

\[
I_i=[L_i,U_i]
=[\rho_i-t_i,\rho_i-1].
\tag{40}
\]

A direct subtraction gives

\[
\boxed{
L_2=L_1+r,
\qquad
U_2=U_1-r.
}
\tag{41}
\]

Thus `I_2` is obtained from `I_1` by deleting exactly `r` integers at each end.

Let `f in K_1 cap K_2`, and define on `I_1`

\[
a_w=f(w\bmod p).
\tag{42}
\]

By (33), `a` has period `g_1` on all of `I_1`. On `I_2` it also has period `g_2`. By (23), (29), and (41), the two trimmed collars are precisely source coordinates that lie in `C_2 setminus C_1`; hence

\[
\boxed{
a_w=0\qquad(w\in I_1\setminus I_2).}
\tag{43}
\]

It remains to show that the two periods force those zeros through the whole central interval.

## 5. The Fine--Wilf threshold is automatic

Set

\[
A:=2c-p.
\tag{44}
\]

For either pair,

\[
A
=2\rho_i-t_i.
\tag{45}
\]

Since `g_i|rho_i` and `g_i|t_i`,

\[
\boxed{g_i\mid A.}
\tag{46}
\]

Also `0<rho_i<t_i`, so

\[
\boxed{|A|<t_i.}
\tag{47}
\]

The number `A` is odd (`p` is odd), hence nonzero. Put

\[
g_0=\gcd(g_1,g_2).
\tag{48}
\]

Because both `g_i` divide `A`,

\[
\operatorname{lcm}(g_1,g_2)\le |A|<t_2.
\tag{49}
\]

Writing `g_1=g_0a`, `g_2=g_0b` with `gcd(a,b)=1`,

\[
g_1+g_2-g_0
=g_0(a+b-1)
\le g_0ab
=\operatorname{lcm}(g_1,g_2),
\tag{50}
\]

because `(a-1)(b-1)>=0`. Therefore

\[
\boxed{
|I_2|=t_2
\ge g_1+g_2-g_0.
}
\tag{51}
\]

The classical Fine--Wilf theorem now implies that the central word `a|_{I_2}`, which has periods `g_1` and `g_2`, also has period

\[
\boxed{g_0.}
\tag{52}
\]

The exact Fine--Wilf threshold is load-bearing here; no asymptotic or generic-position argument is being used.

## 6. One zero collar hits every common-period class

The nesting width has an arithmetic divisibility of its own. Since

\[
r=\rho_1-\rho_2
\tag{53}
\]

and `g_0` divides both `rho_1` and `rho_2`,

\[
\boxed{g_0\mid r.}
\tag{54}
\]

In particular `r>=g_0`. Consider the last `g_0` sites of the lower zero collar,

\[
z\in\{L_2-g_0,\ldots,L_2-1\}.
\tag{55}
\]

They lie in `I_1 setminus I_2`, so `a_z=0`. Equation (49) also gives

\[
g_1<t_2.
\tag{56}
\]

Therefore every translated point `z+g_1` lies in `I_2`: the smallest is at least `L_2`, while the largest is at most `L_2-1+g_1<=U_2`. Since `a` has period `g_1` on `I_1`,

\[
a_{z+g_1}=a_z=0.
\tag{57}
\]

As `z` ranges over the `g_0` consecutive values in (55), the points `z+g_1` give one representative of every residue class modulo `g_0`. By the `g_0`-periodicity (52),

\[
\boxed{a_w=0\qquad(w\in I_2).}
\tag{58}
\]

Together with the collar zeros (43), this kills `a` on all of `I_1`. The source coordinates not represented in `I_1` are precisely `C_1`, which is contained in `C_2` and hence is already zero. Thus `f=0`, proving (9). Notice that the source zero-mean relation (34) is not needed at this stage: the combined equality graph already propagates a forced zero into every component.

Finally, the left kernel of the horizontal concatenation is exactly

\[
\ker_{\rm left}[G_1\;G_2]
=K_1\cap K_2,
\tag{59}
\]

so (9) gives the full source rank (10).

## 7. Stress tests, prior art, and evidence boundary

The proof above was reconstructed independently from the exact WI-096 row-kernel equations and the WI-102 collapsed-rotation theorem. As falsification only, the sign-corrected arithmetic conditions were enumerated over all odd source primes below `180`, all distinct close-prime full-packed positive-defect targets, and every CRT-compatible nearest-boundary sign pair. All `27,180` simultaneous sign-pairs had one common **actual** center after the complement phase correction, satisfied the divisibility and Fine--Wilf inequalities used above, and produced no arithmetic counterexample. This finite check is not used in the proof.

The classical external ingredient is N. J. Fine and H. S. Wilf, **Uniqueness theorems for periodic functions**, *Proceedings of the American Mathematical Society* 16:1 (1965), 109--114, DOI `10.1090/S0002-9939-1965-0174934-9`, which gives exactly the threshold `g_1+g_2-gcd(g_1,g_2)` used in (51)--(52). The later Fine--Wilf/partial-word graph literature is structurally adjacent because it studies propagation of periodicity in the presence of holes, but the present argument needs only the original no-hole theorem on the common central interval. Vaidyanathan's 2014 Ramanujan-subspace papers remain the standard prior art for the surrounding exact-period subspaces and character bases.

A targeted literature search did not locate the specific finite-window statement (9)--(10), the complement-boundary source-phase correction in this shared-kernel use, or the nested-interval reduction of simultaneous full-packed Ramanujan defects to Fine--Wilf periodicity. This negative search is **not** a claim of priority.

The earlier exact finite visualization under `research/visual_exploration/` was useful evidence for the clue but documented its geometry in unsigned canonical `delta_i` charts. For same-sign pairs that coincides with the shared source coordinates. For mixed nearest-boundary signs, equation (14) shows that the source-side phase must be restored before kernel intersections are interpreted. The present theorem does not rely on the visualization's mixed-sign intersection counts.

No Lean formalization currently checks the multi-pair phase normalization, quotient-character pullback, or Fine--Wilf bridge. The exact formalization surface is small: formalize (14)--(24), identify the actual full-packed kernel with a finite word of period `g`, import or prove the finite Fine--Wilf lemma, and certify the collar propagation (53)--(58).

## 8. Program consequence

WI-096 closed the single-pair row-kernel equations, and WI-102 classified the zero-slack endpoint of one residual pair. The present result supplies the first exact **simultaneous/source-labelled consistency law** for that endpoint:

\[
\boxed{
\text{two distinct positive-defect full-packed target edges at one }(p,N)
\Longrightarrow
\text{no shared source defect direction}.
}
\tag{60}
\]

This is strictly stronger information than any scalar pairwise defect count `tau_{p,q}`. A source direction hidden from one fully packed target is necessarily detected by every other distinct simultaneously fully packed target. Equivalently, the pairwise rank losses cannot be charged repeatedly to the same source-kernel vector.

The result does **not** yet yield a Yang covariance estimate or a new zeta-zero proportion. Pairwise trivial intersections also do not by themselves imply that an arbitrary family of three or more defect subspaces forms a direct sum, and weighted signed covariance can still depend on angles and singular values rather than kernel incidence alone. The next substantive aggregation step is therefore to translate (10) into a quantitative lower bound for the locked multi-target covariance at one source, or to extend the same common-center/Fine--Wilf coordinates from exact full packing (`U=0`) to the first positive-slack layers classified by WI-103.