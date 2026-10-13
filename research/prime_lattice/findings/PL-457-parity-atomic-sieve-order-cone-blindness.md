# PL-457 — Parity-preserving atomic sources with sieve-order pair bounds can fail the centered mod-5 cone

**Evidence/status:** EXACT-DERIVED + CLASSICAL PROBABILISTIC METHOD / SOURCE-REALIZABLE NEGATIVE CONTROL.

**Parent findings:** PL-421, PL-445, PL-452, PL-453, PL-454, PL-455, PL-456.

## Claim

Fix any \(1/6<\theta\le 1/2\). There exist \(X\to\infty\), four nonnegative **integer-supported** measures \(\nu_{a,X}\) in reduced residue channels \(a\pmod 5\), and \(H=X^\theta+O(\log X)\) with the following simultaneous properties.

**First moments:** every atom in channel \(a\) is an odd integer congruent to \(a\pmod5\), with weight \((1+o(1))\log X\). For every interval \(I\subset[X,5X/2]\),
\[
\nu_{a,X}(I)=|I|/4+O(\log X).
\tag{1}
\]
Each channel contains \((1/8+o(1))X/\log X\) atoms in \((5X/4,7X/4)\), the rational-prime leading count scale in that fixed interior interval.

**Uniform pair upper bounds:** let \(B_X(d)\) count ordered increasing pairs of *distinct* support sites \(x,x+d\in[X,3X]\), across all four channels. For every integer \(1\le d\le X/2+1\),
\[
B_X(d)=0\quad(d\text{ odd}),\qquad
B_X(d)\ll X/(\log X)^2\quad(d\text{ even}).
\tag{2}
\]
Multiplying by the squared atom weight, the weighted pair sum is \(O(X)\) for every positive shift. This matches the **order and parity exclusion of a Selberg upper bound**, not prime-pair asymptotics, singular-series coefficients, or the genuine prime source.

**Pointwise absolute frame:** define the phase-matched centered windows
\[
R_{a,t}(y)=\int_{(y,y+H]}x^{-it}\,d\nu_{a,X}(x)
-\frac14\int_y^{y+H}x^{-it}\,dx,\qquad
S_{ab}(t)=\int_X^{2X}R_{a,t}(y)\overline{R_{b,t}(y)}\,dy .
\tag{3}
\]
For every \(1\le H\le X/2\), including arbitrary nonintegral lengths, and **every real \(t\)**, an absolute constant \(c_0>0\) satisfies
\[
S(t)\succeq c_0 X\log X\, I_4.
\tag{4}
\]
Thus the same uniform *absolute* pointwise lower-frame phenomenon proved for actual primes in PL-456 survives these matched atomic controls.

**Failure of the normalized gate:** for the chosen polynomial \(H\), at \(t=0\) all Gram diagonals are equal and positive, but with \(C=D^{-1/2}S(0)D^{-1/2}\) and \(D=\operatorname{Diag}S(0)\),
\[
\boxed{\lambda_{\min}(C)\le 1/25<1/4.}
\tag{5}
\]
Hence (1)--(4) do **not** imply the PL-421 inverse-dephasing image-cone floor, even with parity, one heavy atom per logarithmic block, unconditional-sieve-order *upper* bounds at every shift, and uniformly many unpaired jumps.

This is a **logical-information obstruction**, not a counterexample about rational primes, a construction of a Beurling prime system, or a statement about RH.

## One early odd atom per residue per cell

Fix \(c=1/100\). For integers \(N\to\infty\), set
\[
L=20\left\lceil\frac{4\log N}{20}\right\rceil\sim4\log N,\qquad
X=NL,\qquad W=L/4\sim\log X.
\tag{6}
\]
In each block \(I_j=[jL,(j+1)L)\), \(0\le j<3N\), independently pick for each \(a=1,2,3,4\) a uniform offset \(u_{j,a}\) from
\[
\mathcal U_a(L)=\{r_a+10m: m\ge0,\ r_a+10m\le cL\},\qquad
(r_1,r_2,r_3,r_4)=(1,7,3,9).
\tag{7}
\]
For large \(L\), the four sets have cardinality \(\asymp_c L\). Their elements are odd and have residue \(a\bmod5\). Put
\[
\nu_{a,X}=W\sum_{j=0}^{3N-1}\delta_{jL+u_{j,a}} .
\tag{8}
\]
There is exactly one atom of mass \(W\) for each channel in each complete block, always in its first \(cL\) units. Any interval has at most two partial boundary blocks, proving the \(O(L)\) discrepancy in (1). Counting the \(\asymp X/(2L)\) interior blocks and using \(L\sim4\log X\) proves the asserted atom count.

## Simultaneous sieve-order bounds by bounded differences

Fix \(d\ge1\). Any two source atoms from blocks \(j,j'\) with gap \(d\) obey
\[
|d-(j'-j)L|\le cL<L/2 .
\tag{9}
\]
For each starting block, there is at most one possible difference \(j'-j\), and at most \(16\) possible ordered channel pairs. Except for the impossible same-atom case \(d>0\), the two sampled offsets are independent; conditional on the first offset, at most one choice of the second realizes the prescribed gap. As \(\min_a|\mathcal U_a(L)|\gg_c L\), and the number of starting blocks is \(O(X/L)\),
\[
\mathbb E B_X(d)\ll_c X/L^2 .
\tag{10}
\]
All support sites are odd, so \(B_X(d)=0\) for odd \(d\).

Changing one of the \(O(X/L)\) independent offsets can destroy or create at most the incoming and outgoing \(d\)-pairs of its old and new atom locations, changing \(B_X(d)\) by at most \(4\). McDiarmid's classical bounded-differences inequality (1989, SOURCES item 117) therefore gives constants \(K_c,\gamma_c>0\) with
\[
\mathbb P\{B_X(d)>K_cX/L^2\}
\le\exp(-\gamma_c X/L^3).
\tag{11}
\]
A union bound over the \(O(X)\) integer shifts \(1\le d\le X/2+1\) tends to zero. Fix one realization satisfying the bound **for every shift at once**, giving (2). The construction uses no prime theorem; in particular it does not reproduce the actual Hardy--Littlewood singular series.

## Isolated jumps imply a uniform absolute frame

Every channel contains \(X/(2L)+O(1)\) atoms in \(J=(5X/4,7X/4)\). For arbitrary \(1\le H\le X/2\), let \(m=\lfloor H\rfloor\) and exclude interior atoms \(x\) for which either \(x+m\) or \(x+m+1\) is another support atom. Since all those translated pairs lie in \([X,3X]\), (2) excludes at most
\[
B_X(m)+B_X(m+1)\ll X/L^2=o(X/L)
\tag{12}
\]
atoms before splitting by residue. Consequently each channel has at least \(X/(4L)\) good interior atoms, **uniformly in \(H\)**.

For \(z\in\mathbb C^4\) set \(F_z(y)=\sum_a\overline{z_a}R_{a,t}(y)\) and \(\kappa=\frac14\sum_a\overline{z_a}\). Around any good atom \(x\), the interval \((x-h,x+h)\), \(h=1/4\), contains exactly one outgoing atom jump, at \(y=x\), of magnitude \(W|z_{a(x)}|\). All outgoing atoms lie at distinct integers; an incoming jump at \(n-H\) in that neighborhood would require \(n=x+m\) or \(x+m+1\), which were excluded. The continuum term \(Q_t(y)=\int_y^{y+H}v^{-it}dv\) is smooth and
\[
Q_t'(y)=(y+H)^{-it}-y^{-it},\qquad |Q_t'(y)|\le2
\quad(t\in\mathbb R).
\tag{13}
\]
Let \(\mu_x^\pm\) be the means of \(F_z\) on the two adjacent half-neighborhoods. Then
\[
D_x=\mu_x^+-\mu_x^-=
-\overline{z_{a(x)}}W x^{-it}+e_x,\qquad
|e_x|\le h\|z\|_2.
\tag{14}
\]
The half-neighborhoods are disjoint across good atoms. Jensen, followed by \(|v+w|^2\ge|v|^2/2-|w|^2\), gives
\[
\begin{aligned}
z^*S(t)z
&\ge\frac h2\sum_{x\ \mathrm{good}}|D_x|^2\\
&\ge\frac h2\left[
\frac{W^2}{2}\sum_a\#G_a(H)|z_a|^2
-h^2\#G(H)\|z\|_2^2\right]\\
&\ge \frac{XL}{2048}\|z\|_2^2
\quad\text{for large }X,
\end{aligned}
\tag{15}
\]
using \(\#G_a(H)\ge X/(4L)\), \(\#G(H)\le3X/L\), \(h=1/4\), and \(W=L/4\). As \(L\asymp\log X\), this proves (4). Notice this floor is **absolute**; it makes no claim about the ratio to the diagonal energy.

## Exact normalized common-mode collapse at a half-cell window

Let
\[
k=\lfloor X^\theta/L\rfloor\ge1,\qquad
H=(k+\tfrac12)L=X^\theta+O(L),\qquad H\le X/2.
\tag{16}
\]
Because \(20\mid L\), this \(H\) is integral. For almost every \(y=jL+v\), \(0\le v<L\), the number \(N_a(y)\) of atoms of channel \(a\) in \((y,y+H]\) is exactly
\[
N_a(y)=
\begin{cases}
k+\mathbf1_{\{v<u_{j,a}\}},&0\le v<L/2,\\
k+\mathbf1_{\{u_{j+k+1,a}\le v-L/2\}},&L/2\le v<L.
\end{cases}
\tag{17}
\]
Thus \(N_a(y)\in\{k,k+1\}\) always. At \(t=0\), the matched continuum subtraction equals \(H/4=W(k+1/2)\), so
\[
R_{a,0}(y)=W(N_a(y)-k-\tfrac12)\in\{-W/2,+W/2\},\qquad
S_{aa}(0)=XW^2/4 .
\tag{18}
\]
Outside the within-cell exceptional strips \([0,cL]\) and \([L/2,L/2+cL]\), every channel's sign is the **same**: negative for \(v\in(cL,L/2)\), positive for \(v\in(L/2+cL,L)\). Since \([X,2X]\) is exactly \(N\) whole blocks, the exceptional set occupies at most fraction \(2c\) of origins. Hence each normalized off-diagonal entry, an average of products of signs, obeys
\[
C_{ab}\ge1-2(2c)=1-4c=24/25,\qquad a\ne b.
\tag{19}
\]
The unit vector \((1,-1,0,0)/\sqrt2\) then gives
\[
\lambda_{\min}(C)\le1-C_{12}\le4c=1/25<1/4 ,
\tag{20}
\]
proving the advertised failure for **every** allowed realization, including the one satisfying (2) and (4).

## Prior art, falsification, and boundary of relevance

PL-452 proved that arbitrarily strong *first-order* short-progression control fails to decide the normalized centered Gram, using **diffuse** matched sources. PL-455--PL-456 then showed the genuine atomic von-Mangoldt source has qualitative and uniform *absolute* pointwise frames from unpaired outgoing jumps. The present stronger matched-control obstruction establishes that **even preserving** isolated integer atom jumps, prime-count-order number of atoms, parity, sieve-*order upper* pair counts at all shifts, and the PL-456 absolute frame does **not** force the PL-421 normalized \(1/4\) image cone at a polynomial window. The source-specific second-order *relative and oriented* covariance remains indispensable.

The probabilistic selection uses classical McDiarmid bounded differences (SOURCES item 117); the comparison sieve is Lichtman--Teräväinen (2022, item 115). No novelty is claimed for these ingredients or for the general block-jitter technique. The line-specific conclusion is the precise **simultaneous** mod-5 countercontrol to an inference from these explicitly listed inputs. The constructed sources need not have the actual prime-gap law, singular-series main terms, completely multiplicative structure, or any continuation/zero-divisor bridge. Stronger genuine-prime arithmetic hypotheses could exclude them. Failure is exhibited at \(t=0\), not asserted for all vertical averages, and the PL-418 signed source-subtracted form is distinct. There is no RH implication.