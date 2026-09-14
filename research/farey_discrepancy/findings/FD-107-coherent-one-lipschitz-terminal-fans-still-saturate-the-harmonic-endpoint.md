# FD-107 — coherent one-Lipschitz terminal fans still saturate the harmonic endpoint

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIXED-COHERENT-SOURCE + ONE-LIPSCHITZ + POLYNOMIAL-HIGH-MASS + DYADIC-TERMINAL-DOMINANCE + LEAST-PRIME-PARTITION + FULL-CHILD-STRESS-TEST + CRITICAL-ENDPOINT-FAILURE + PHYSICAL-COEFFICIENT-LAW-FRONTIER`.

`FD-106` localizes the only scale-dependent loss in critical excess-mass transport to the repaired dyadic-terminal family. There the complete odd-squarefree terminal prefix is partitioned by least prime factor `p`, repaired child horizons satisfy `C_p/H=(1+o(1))/p`, and aggregate packet mass alone gives only the `epsilon>0` law because `sum_p 1/p` diverges. Two pieces of structure remained unused: every packet is cut from one common quotient-shell source, and that source is one-Lipschitz.

Those two generic coherence properties still do **not** remove the harmonic endpoint. There exists one fixed nonnegative source

\[
F:\mathbb Z_{\ge0}\to\mathbb R_{\ge0},
\qquad F(0)=0,\quad F(1)=1,\quad |F(n+1)-F(n)|\le1,
\tag{1}
\]

with the sublinear envelope

\[
F(n)\ll n^{3/4},
\tag{2}
\]

and an unbounded sequence of parent horizons `H_j` for which:

1. the nonsquarefree mass is polynomially above the linear floor,
   \[
   U^F_{H_j}=H_j^{6/5+o(1)};
   \tag{3}
   \]
2. a `1-o(1)` fraction of that mass lies in the **exact dyadic-terminal nonhead family** `r=4p`, with `p` odd prime, so the deterministic least-prime-factor partition is present rather than relaxed;
3. every current terminal coordinate lies far above the adaptive source cutoff `L_H=U_H/(H\log H)` from `FD-105`;
4. for every repaired child `C_{p,j}=4 floor(B_j/p)`, with `H_j=4B_j`, the **complete child state** satisfies
   \[
   \boxed{
   \sup_{3\le p\le P_j}
   \frac{U^F_{C_{p,j}}/C_{p,j}}
        {U^F_{H_j}/H_j}
   \longrightarrow0.
   }
   \tag{4}
   \]

More precisely the ratio in (4) is `O(1/S_j)`, where

\[
S_j:=\sum_{3\le p\le P_j}\frac1p\longrightarrow\infty.
\tag{5}
\]

Thus the matched harmonic allocation from `FD-106` can be realized by a **single fixed coherent one-Lipschitz shell source**, while the terminal family dominates a genuine polynomial high-mass state and while all extra energy already present in each repaired child remains negligible. The endpoint obstruction is therefore not an artifact of allowing arbitrary independent packet masses.

The synthetic `F` is not the physical quotient-shell source `\mathcal H`. In particular it is not required to satisfy

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\tag{6}
\]

Consequently the durable boundary is sharp: removing the `epsilon` in `FD-106` requires arithmetic information at least as strong as a genuine consequence of (6), or another physical-source restriction not implied by common shell values, bounded increments, sublinear growth, high mass, and the exact least-prime-factor terminal partition.

## 1. A lacunary coherent source with many reciprocal prime tents

Choose recursively very large integers `B_j` and put

\[
H_j:=4B_j,
\qquad
P_j:=\lfloor B_j^{1/5}\rfloor,
\qquad
A_j:=\left\lfloor\frac{B_j}{1000P_j^2}\right\rfloor.
\tag{7}
\]

For every odd prime `p<=P_j` define the reciprocal-shell center

\[
k_{j,p}:=\left\lfloor\frac{B_j}{p}\right\rfloor
\tag{8}
\]

and the height

\[
a_{j,p}:=rac{A_j}{\sqrt{p\,w(p)}},
\qquad
w(r):=\frac{J_2(r)}{r^2}.
\tag{9}
\]

Put a slope-one triangular tent at each center,

\[
T_{j,p}(n):=(a_{j,p}-|n-k_{j,p}|)_+.
\tag{10}
\]

For distinct integers `m,n<=P_j`,

\[
\left|\frac{B_j}{m}-\frac{B_j}{n}\right|
\ge \frac{B_j}{P_j^2},
\tag{11}
\]

so after the floor errors the reciprocal sample points remain separated by more than `100 A_j` once `j` is large. Since `a_(j,p)<A_j`, all tents in one block are disjoint and every reciprocal sample `floor(B_j/m)` with `m\ne p` lies outside the `p`-tent.

Choose `B_(j+1)` sufficiently large that the next block begins above the entire support of all previous blocks and, writing

\[
Q_{<j}:=
\sum_{n\text{ in previous blocks}}
\frac{F(n)^2}{n(n+1)},
\tag{12}
\]

also ensure

\[
K_{<j}^2=o(B_j^{4/5}),
\qquad
Q_{<j}=o(B_j^{1/5}),
\tag{13}
\]

where `K_<j` is the largest previous support index. This is possible because only finitely many values have been chosen before stage `j`. Define

\[
F(n):=\mathbf 1_{\{n=1\}}+\sum_{j,p}T_{j,p}(n).
\tag{14}
\]

The supports are disjoint and separated by zero gaps, so (1) is exact. On block `j`, every nonzero point has

\[
n\gg B_j/P_j=B_j^{4/5},
\qquad
F(n)\le A_j\ll B_j^{3/5},
\tag{15}
\]

which gives the global envelope (2).

The construction is fixed once the lacunary sequence `B_j` is chosen; it is not an horizon-by-horizon choice of independent packet amplitudes.

## 2. At the parent horizon each current tent is sampled only by row `4p`

Consider the synthetic Jordan mass

\[
U_H^F
:=
\sum_{\substack{1<r\le H\\\mu(r)=0}}
 w(r)F\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2.
\tag{16}
\]

Fix a current prime `p<=P_j`. The row `r=4p` samples its center exactly:

\[
\left\lfloor\frac{H_j}{4p}\right\rfloor
=
\left\lfloor\frac{B_j}{p}\right\rfloor
=k_{j,p}.
\tag{17}
\]

No other integer row samples that tent. Indeed, if `r\ne4p`, then

\[
\left|\frac{4B_j}{r}-\frac{B_j}{p}\right|
=
\frac{B_j|4p-r|}{rp}.
\tag{18}
\]

If the two quotients were within `A_j+2`, then for large `j` necessarily `r<=8p`; equation (18) would then be at least

\[
\frac{B_j}{8p^2}
\ge
\frac{B_j}{8P_j^2}
>100A_j,
\tag{19}
\]

a contradiction after the two floor errors. Thus the current block contributes to `U_(H_j)^F` exactly through the rows `4p`.

These rows are precisely the dyadic-terminal nonhead rows of `FD-093`: under the smallest-repeated-prime assignment they belong to the `2^2` branch, first-deflate to `2p`, and the latter is squarefree. Their current total mass is

\[
\begin{aligned}
U_{H_j}^{\rm cur}
&=
\sum_{3\le p\le P_j}
 w(4p)a_{j,p}^2\\
&=
\frac34A_j^2
\sum_{3\le p\le P_j}\frac1p\\
&=
\boxed{\frac34A_j^2S_j}.
\end{aligned}
\tag{20}
\]

The head atom `m=1` is absent because the current block has no tent at `B_j`.

Future blocks are invisible at `H_j` by construction. For the old blocks, if `X>=B_j^{4/5}` then (13) gives `X>=K_<j(K_<j+1)` and the exact quotient-shell count implies

\[
\#\{r:\lfloor X/r\rfloor=n\}
\le
\frac{2X}{n(n+1)}
\tag{21}
\]

for every old support point. Since `w(r)<=1`,

\[
U_X^{F,\rm old}\le2XQ_{<j}.
\tag{22}
\]

At `X=H_j`, equations (13), (20), and `A_j^2/B_j\asymp B_j^{1/5}` give

\[
U_{H_j}^F
=
\left(\frac34+o(1)\right)A_j^2S_j.
\tag{23}
\]

Euler's elementary divergence of the reciprocal-prime sum, already used in `FD-106`, gives `S_j->infinity`. Since `A_j=B_j^{3/5+o(1)}`,

\[
\boxed{
U_{H_j}^F
=B_j^{6/5+o(1)}
=H_j^{6/5+o(1)}.
}
\tag{24}
\]

Thus the countermodel lies polynomially above the exact linear mass floor rather than exploiting a marginal low-mass regime.

## 3. The whole current family is source-rich

The adaptive source threshold from `FD-105` is

\[
L_{H_j}^F
:=
\left\lfloor
\frac{U_{H_j}^F}{H_j\log H_j}
\right\rfloor
=
B_j^{1/5+o(1)}.
\tag{25}
\]

Every current terminal row samples

\[
k_{j,p}
\ge
\frac{B_j}{P_j}-1
=B_j^{4/5+o(1)}.
\tag{26}
\]

Hence

\[
\min_{p\le P_j}
\frac{k_{j,p}}{L_{H_j}^F}
\longrightarrow\infty.
\tag{27}
\]

So the failure below survives the exact source-rich truncation that powers `FD-105` and `FD-106`; it is not generated by energy hidden near bounded quotient arguments.

## 4. Every repaired child sees only its own current tent

For the row `m=p` in the terminal prefix, the `FD-093` repair has `t=1` and

\[
C_{p,j}:=4\left\lfloor\frac{B_j}{p}\right\rfloor
=4k_{j,p}.
\tag{28}
\]

The destination row `4` therefore samples the same source value exactly:

\[
\left\lfloor\frac{C_{p,j}}4\right\rfloor
=k_{j,p}.
\tag{29}
\]

More importantly, the **complete child state** does not pick up another current tent. Suppose a row `r>=2` at `C_(p,j)` sampled the `q`-tent. Comparing the unfloored quotients gives

\[
\left|\frac{4B_j}{pr}-\frac{B_j}{q}\right|
=
\frac{B_j|4q-pr|}{prq}.
\tag{30}
\]

Unless `4q=pr`, closeness within `A_j+O(1)` forces `r<=8q/p` and therefore makes (30) at least

\[
\frac{B_j}{8q^2}
\ge
\frac{B_j}{8P_j^2}
>100A_j,
\tag{31}
\]

again impossible after the floor errors. If `4q=pr`, then the odd primality of `p,q` forces `p=q` and `r=4`. Thus the own destination row is the unique sampler of all current tents in the whole child state.

Its current child mass is exactly

\[
U_{C_{p,j}}^{F,\rm cur}
=
\frac34a_{j,p}^2
=
\frac{3A_j^2}{4p\,w(p)}.
\tag{32}
\]

Uniformly for `p<=P_j`,

\[
C_{p,j}
=
\frac{4B_j}{p}(1+o(1)),
\tag{33}
\]

and `w(p)=1-p^{-2}>=8/9`. The old-block bound (22) applies uniformly because the smallest child is `B_j^{4/5+o(1)}` and (13) was chosen for that scale. Hence

\[
\frac{U_{C_{p,j}}^F}{C_{p,j}}
\le
\left(
\frac{3}{16w(p)}+o(1)
\right)
\frac{A_j^2}{B_j},
\tag{34}
\]

where the `o(1)` is uniform over all current primes.

On the other hand, (23) gives

\[
\frac{U_{H_j}^F}{H_j}
=
\left(
\frac{3}{16}+o(1)
\right)
\frac{A_j^2}{B_j}S_j.
\tag{35}
\]

Dividing (34) by (35),

\[
\boxed{
\sup_{3\le p\le P_j}
\frac{U_{C_{p,j}}^F/C_{p,j}}
     {U_{H_j}^F/H_j}
\le
\frac{9/8+o(1)}{S_j}
\longrightarrow0.
}
\tag{36}
\]

This proves (4). It is stronger than the abstract matched allocation in `FD-106`: the packet masses are generated by one fixed coherent source, the parent high-mass state is terminal-dominated, and the estimate uses the full child masses rather than only the repaired masks `N_(p,H)<=U_(C_p)`.

## 5. Exact relation to the `FD-106` harmonic endpoint

Inside the terminal prefix, every composite odd-squarefree row samples zero from the current block, while the prime row `m=p` contributes

\[
Q_{p,j}
=w(p)a_{j,p}^2
=rac{A_j^2}{p}.
\tag{37}
\]

The exact repair factor from `FD-093` is

\[
\gamma_p
=
\frac{3/4}{1-p^{-2}},
\]

so

\[
N_{p,j}
=\gamma_pQ_{p,j}
=rac{3A_j^2}{4p\,w(p)}.
\tag{38}
\]

Thus the coherent source realizes, up to the bounded exact Jordan factor, precisely the harmonic packet profile

\[
N_{p,j}\asymp\frac{A_j^2}{p}
\tag{39}
\]

that makes the critical contraction sum diverge. Since `C_(p,j)/H_j=(1+o(1))/p`, each individual child's critical excess is of order `A_j^2/B_j`, while the parent has the extra factor `S_j`. This is exactly the entropy deficit that the positive power `(C/H)^epsilon` pays in `FD-106`.

The result does **not** say that the physical `mathcal H` realizes this allocation. It says that three natural attempts to remove the epsilon are now ruled out simultaneously: using only the deterministic least-prime-factor partition, using only the fact that all packets sample one common shell function, or adding the exact generic source bounds `|Delta F|<=1` and `F(n)<<n^(3/4)` together with polynomial high mass. All of them admit the same terminal harmonic failure.

## 6. Stress test, prior art, and remaining boundary

There are three fragile points in the construction, and each is exposed by an exact check.

First, reciprocal-shell isolation is not a cardinality heuristic. Equations (18)--(19) show that the integer separation between the target row and every competing parent row is much larger than the tent width. Second, child isolation is stronger: equation (30) reduces a possible collision to the integer equation `4q=pr`, whose only solution for odd primes is the intended `p=q,r=4`. Third, old source blocks are controlled in the **complete** parent and child states by the quotient-shell counting estimate (21), while lacunarity makes future blocks invisible. Thus no hidden nonterminal or cross-packet child energy repairs (36).

The exponent `1/5` is convenient, not canonical. More generally one may take `P=B^alpha` and tent width `A<<B/P^2`; the resulting terminal mass has `U_H/H\asymp B^(1-4alpha) sum_(p<=P)1/p`, so any fixed `0<alpha<1/4` gives polynomial high mass. The particular choice `alpha=1/5` makes the displayed scales transparent.

A targeted literature audit found the expected classical neighboring objects: Buchstab/least-prime-factor decompositions of sifted or squarefree sets, weighted sieve variants, and Farey discrepancy formulas using Möbius summation. Those results concern counting or multiplicative weights on integer sets; they do not supply a theorem forbidding a coherent reciprocal-shell profile of the form above. No novelty is claimed for least-prime-factor partitioning, reciprocal-prime divergence, or triangular Lipschitz tents individually. The Mathia-specific content is the implication separation at the exact `FD-106` endpoint. No external theorem is load-bearing, so `SOURCES.md` needs no new anchor.

The countermodel is falsified if the tents cannot be made globally one-Lipschitz, if any current parent tent is sampled outside `r=4p`, if a repaired child samples a different current tent, if old blocks contribute non-negligible critical excess uniformly over the child fan, or if the terminal parent mass fails to be polynomially superlinear. Equations (11)--(36) address those points directly.

The result must **not** be cited as a counterexample for the physical Mertens/Farey source. Its role is to sharpen the next theorem. After `FD-107`, a critical-lossless terminal predecessor cannot follow from generic shell coherence. It must exploit the exact physical increment law (6), an equivalent divisibility/multiplicative constraint, or another arithmetic statement strong enough to forbid reciprocal prime tents across one complete source prefix. This is now the precise endpoint left by `FD-106`.
